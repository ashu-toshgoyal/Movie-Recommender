# 🎬 Climaz  
### *Mood-Based Bollywood Movie Recommendation System*

<p align="center">
  <b>Smart • Explainable • Interactive • Learning-Based</b>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge">
  <img src="https://img.shields.io/badge/Pandas-Data%20Processing-green?style=for-the-badge">
  <img src="https://img.shields.io/badge/Tkinter-GUI-orange?style=for-the-badge">
  <img src="https://img.shields.io/badge/Bollywood-Dataset-red?style=for-the-badge">
</p>

---

## 📌 Overview

**Climaz** is a **mood-based, intent-aware Bollywood movie recommendation system** built using **Python, Pandas, and Tkinter**.

Unlike traditional black-box ML recommenders, Climaz uses:

- 🧠 **Human-like reasoning**
- 🔍 **Text similarity & intent extraction**
- 👍 👎 ❤️ **User feedback learning**
- 📊 **Explainable scoring**

> Climaz does not just recommend movies —  
> it understands *why* a movie should be recommended.

---

## ✨ Features

### 🔎 Smart Text Understanding
- Extracts **actors**, **genres**, and **keywords**
- Removes noise using **stop-words**
- Handles free-form user input

### 🎯 Correct Semantic Ranking
- Actor-pair boosting (e.g. *Salman + Aamir → Andaz Apna Apna*)
- Weighted scoring (actors > keywords > genres)
- Prevents irrelevant matches from ranking high

### 🔁 Learning From Feedback
- 👍 Like → increases preference
- 👎 Dislike → reduces preference
- ❤️ Favourite → strong positive bias
- Feedback is **persisted** in `database.csv`

### 🪟 Clean GUI
- Minimal Apple-style Tkinter UI
- Icon-only buttons
- Responsive layout

### 📖 Explainable Logic
- No hidden ML magic
- Every recommendation has a reason
- Easy to debug, tune, and extend

---

## 🧠 How Climaz Works (High Level)

