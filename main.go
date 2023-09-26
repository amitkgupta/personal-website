package main

import (
	"bytes"
	"fmt"
	"html/template"
	"io"
	"log"
	"net/http"
	"os"
	"regexp"

	"github.com/amitkgupta/go-smarthealthcards/v2/ecdsa"
	"github.com/amitkgupta/go-smarthealthcards/v2/webhandlers"
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

	shcWebHandlers := webhandlers.New(shcKey, "https://akgupta.ca/smart-health-cards")

	template413, err := template.ParseFiles("413.html.tmpl")
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

			if r.Host == "www.akgupta.ca" {
				u := r.URL
				u.Host = "akgupta.ca"
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
				"/ms-icon-70x70.png",
				"/dcsd-2023-mlo/nav.gif",
				"/dcsd-2023-mlo/keypad.gif",
				"/dcsd-2023-mlo/styles.css",
				"/dcsd-2023-mlo/script.js":
				http.ServeFile(w, r, r.URL.Path[1:])
			case "/":
				http.ServeFile(w, r, "index.html")
			case "/dcsd-2023-mlo", "/dcsd-2023-mlo/":
				http.ServeFile(w, r, "dcsd-2023-mlo/presentation.html")
			case "/smart-health-cards", "/smart-health-cards/":
				switch r.Method {
				case http.MethodGet:
					http.ServeFile(w, r, "smart-health-cards-form.html")
				case http.MethodPost:
					responseCode, errorMessage, ok := shcWebHandlers.ProcessForm(w, r)
					if ok {
						return
					}

					switch responseCode {
					case http.StatusInternalServerError:
						http.ServeFile(w, r, "500.html")
						w.WriteHeader(http.StatusInternalServerError)
					case http.StatusRequestEntityTooLarge:
						buf := new(bytes.Buffer)
						if err := template413.Execute(buf, errorMessage); err != nil {
							http.ServeFile(w, r, "500.html")
							w.WriteHeader(http.StatusInternalServerError)
						} else {
							io.Copy(w, buf)
							w.WriteHeader(http.StatusRequestEntityTooLarge)
						}
					default:
						http.Error(w, errorMessage, responseCode)
					}
				default:
					http.Error(w, fmt.Sprintf("%s method not allowed", r.Method), http.StatusMethodNotAllowed)
				}
			case "/smart-health-cards/.well-known/jwks.json":
				responseCode, errorMessage, ok := shcWebHandlers.JWKSJSON(w)
				if ok {
					return
				}

				if responseCode == http.StatusInternalServerError {
					http.ServeFile(w, r, "500.html")
					w.WriteHeader(http.StatusInternalServerError)
				} else {
					http.Error(w, errorMessage, responseCode)
				}
			default:
				http.ServeFile(w, r, "404.html")
				w.WriteHeader(http.StatusNotFound)
			}
		}),
	))
}
