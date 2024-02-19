// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getFirestore } from 'firebase/firestore'
import { getAuth } from 'firebase/auth'
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
const firebaseConfig = {
  apiKey: "AIzaSyBhvQgllHQEtBkoAyFDNxCY_VYFXsWKrqY",
  authDomain: "umasebenta-2019122.firebaseapp.com",
  projectId: "umasebenta-2019122",
  storageBucket: "umasebenta-2019122.appspot.com",
  messagingSenderId: "1046187376387",
  appId: "1:1046187376387:web:1654196bacb593b7ffb336"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const db = getFirestore(app);
const auth = getAuth(app);

export {
    db,
    auth
}