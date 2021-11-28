package main

import (
	"encoding/json"
	"errors"
	"fmt"
	"log"
	"net/http"
	"os"
	"regexp"

	"github.com/amitkgupta/personal-website/smarthealthcards/ecdsa"
	"github.com/amitkgupta/personal-website/smarthealthcards/fhirbundle"
	"github.com/amitkgupta/personal-website/smarthealthcards/jws"
	"github.com/amitkgupta/personal-website/smarthealthcards/qrcode"
	"github.com/amitkgupta/personal-website/smarthealthcards/web"
)

func main() {
	pattern := regexp.MustCompile(`^/(blog/.*|images/.*|sitemap.xml|atom.xml)$`)

	shcKey, err := ecdsa.LoadKey(
		os.Getenv("SMART_HEALTH_CARDS_KEY_D"),
		os.Getenv("SMART_HEALTH_CARDS_KEY_X"),
		os.Getenv("SMART_HEALTH_CARDS_KEY_Y"),
	)
	if err != nil {
		log.Fatal(err)
	}

	log.Fatal(http.ListenAndServe(
		":"+os.Getenv("PORT"),
		http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
			if r.Header.Get("X-Forwarded-Proto") == "http" {
				u := r.URL
				u.Scheme = "https"
				u.Host = r.Host
				http.Redirect(w, r, u.String(), http.StatusMovedPermanently)
				return
			}

			if pattern.MatchString(r.URL.Path) {
				u := r.URL
				u.Host = "legacy-blog.akgupta.ca"
				http.Redirect(w, r, u.String(), http.StatusMovedPermanently)
				return
			}

			switch r.URL.Path {
			case "/android-icon-144x144.png",
				"/android-icon-192x192.png",
				"/android-icon-36x36.png",
				"/android-icon-48x48.png",
				"/android-icon-72x72.png",
				"/android-icon-96x96.png",
				"/apple-icon-114x114.png",
				"/apple-icon-120x120.png",
				"/apple-icon-144x144.png",
				"/apple-icon-152x152.png",
				"/apple-icon-180x180.png",
				"/apple-icon-57x57.png",
				"/apple-icon-60x60.png",
				"/apple-icon-72x72.png",
				"/apple-icon-76x76.png",
				"/apple-icon-precomposed.png",
				"/apple-icon.png",
				"/browserconfig.xml",
				"/favicon-16x16.png",
				"/favicon-32x32.png",
				"/favicon-96x96.png",
				"/favicon.ico",
				"/manifest.json",
				"/mosswall.jpg",
				"/ms-icon-144x144.png",
				"/ms-icon-150x150.png",
				"/ms-icon-310x310.png",
				"/ms-icon-70x70.png":
				http.ServeFile(w, r, r.URL.Path[1:])
			case "/":
				http.ServeFile(w, r, "index.html")
			case "/smart-health-cards":
				switch r.Method {
				case http.MethodGet:
					http.ServeFile(w, r, "smarthealthcards/form.html")
				case http.MethodPost:
			        fhirBundle, err := web.ParseInput(r)
			        if err != nil {
			            http.Error(w, err.Error(), http.StatusBadRequest)
			            return
			        }

			        payload, err := json.Marshal(fhirbundle.NewJWSPayload(fhirBundle))
			        if err != nil {
			            http.ServeFile(w, r, "500.html")
			            w.WriteHeader(http.StatusInternalServerError)
			            return
			        }

			        healthCardJWS, err := jws.SignAndSerialize(payload, shcKey)
			        if err != nil {
			            http.ServeFile(w, r, "500.html")
			            w.WriteHeader(http.StatusInternalServerError)
			            return
			        }

			        qrPNG, err := qrcode.Encode(healthCardJWS)
			        if err != nil {
			            if errors.Is(err, qrcode.JWSTooLargeError) {
			                http.ServeFile(w, r, "smarthealthcards/413.html")
			                w.WriteHeader(http.StatusRequestEntityTooLarge)
			            } else {
			                http.ServeFile(w, r, "500.html")
			                w.WriteHeader(http.StatusInternalServerError)
			            }
			            return
			        }

			        w.Header().Set("Content-Type", "image/png")
			        w.Write(qrPNG)
				default:
					http.Error(w, fmt.Sprintf("%d method not allowed", r.Method), http.StatusMethodNotAllowed)
				}
			case "/smart-health-cards/.well-known/jwks.json":
				if jwksJSON, err := shcKey.JWKSJSON(); err != nil {
		            http.ServeFile(w, r, "500.html")
		            w.WriteHeader(http.StatusInternalServerError)
				} else {
					w.Header().Set("Access-Control-Allow-Origin", "*")
					w.Header().Set("Content-Type", "application/json")
					w.Write(jwksJSON)
				}
			default:
				http.ServeFile(w, r, "404.html")
				w.WriteHeader(http.StatusNotFound)
			}
		}),
	))
}
