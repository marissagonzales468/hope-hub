// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
const firebaseConfig = {
  apiKey: "AIzaSyBMb2ABFOG61Tf7OeCq0tkXoV_njDEWkJo",
  authDomain: "hopehub-26dbb.firebaseapp.com",
  projectId: "hopehub-26dbb",
  storageBucket: "hopehub-26dbb.firebasestorage.app",
  messagingSenderId: "610728106110",
  appId: "1:610728106110:web:c7f5c8e00f25fae3e7e02f"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const db = firebase.firestore();