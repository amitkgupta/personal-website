package main

import (
	"log"
	"net/http"
	"os"
	"regexp"
)

func main() {
	pattern := regexp.MustCompile(`^/(blog/.*|images/.*|sitemap.xml|atom.xml)$`)

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
			case "/404.jpg",
				"/android-icon-144x144.png",
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
			default:
				w.WriteHeader(http.StatusNotFound)
				http.ServeFile(w, r, "404.html")
			}
		}),
	))
}
