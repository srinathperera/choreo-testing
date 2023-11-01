package main

import (
	"encoding/json"
	"fmt"
	"log"
	"net/http"
)

type Profile struct {
	Name    string `json:"name"`
	Age     int    `json:"age"`
	Country string `json:"country"`
}

func getHandler(w http.ResponseWriter, r *http.Request) {
	name := r.URL.Query().Get("name")
	if name == "" {
		name = "World"
	}
	response := fmt.Sprintf("Hello, %s!", name)
	w.Write([]byte(response))
}

func updateProfileHandler(w http.ResponseWriter, r *http.Request) {
	var profile Profile
	err := json.NewDecoder(r.Body).Decode(&profile)
	if err != nil {
		http.Error(w, err.Error(), http.StatusBadRequest)
		return
	}

	response := fmt.Sprintf("Profile updated: Name - %s, Age - %d, Country - %s", profile.Name, profile.Age, profile.Country)
	w.Header().Set("Content-Type", "application/json")
	json.NewEncoder(w).Encode(map[string]string{"message": response})
}

func main() {
	http.HandleFunc("/get", getHandler)
	http.HandleFunc("/updateprofile", updateProfileHandler)

	fmt.Println("Server is running on port 8080")
	log.Fatal(http.ListenAndServe(":8080", nil))
}
