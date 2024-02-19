// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getFirestore } from 'firebase/firestore';
import { getAuth } from 'firebase/auth'
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
const firebaseConfig = {
  apiKey: "AIzaSyDOYylsHRV5M6PNi-h7_mIU9GKToHUEpOU",
  authDomain: "projeto-2---2019122.firebaseapp.com",
  projectId: "projeto-2---2019122",
  storageBucket: "projeto-2---2019122.appspot.com",
  messagingSenderId: "827351094606",
  appId: "1:827351094606:web:63f34382d5046fe974ba1f"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const db = getFirestore(app);
const auth = getAuth(app);

export {
    db,
    auth
}