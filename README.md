# BMI_Calculator


## Introduction

This is a Python-based GUI application that allows users to calculate their Body Mass Index (BMI) and store the data in an SQLite database. The application is built using Tkinter for the graphical interface, Matplotlib for data visualization, and SQLite for storing user data. Users can track their BMI over time and visualize the trend using interactive plots.

## Features

 1. BMI Calculation: Calculates BMI using weight and height inputs.
 2. Health Categorization: Classifies BMI into categories (Underweight, Normal, Overweight, Obese).
 3. Database Storage: Stores user BMI data in an SQLite database.
 4. Historical Data Visualization: Displays BMI trends for individual users using Matplotlib.
 5. Full-Screen GUI: Provides a full-screen user interface with customizable themes.

## Prerequisites
Ensure you have the following libraries installed before running the application:

    pip install tkinter
    pip install matplotlib
    pip install sqlite3
    pip install ttkthemes

## File Structure

 1. bmi_data.db: SQLite database file to store user records.
 2. main.py: Main script to run the application.


## Key Functionalities
### 1. BMI Calculation Logic:

 - Converts height from cm to meters and calculates BMI using the formula:

 - Rounds the result to 2 decimal places.
### 2. BMI Categorization:

 1. Classifies the BMI value into the following categories:
    - Underweight: BMI < 18.5
    - Normal: 18.5 ≤ BMI < 24.9
    - Overweight: 25 ≤ BMI < 29.9
    - Obese: BMI ≥ 30

### 3. Saving Data to Database:
 1. Saves the user’s name, weight, height, BMI, and timestamp to an SQLite database (bmi_data.db).
 2. Automatically creates the bmi_records table if it doesn’t exist.

### 4. View Historical Data:

 1. Displays a list of users and allows the selection of an individual user to visualize their BMI trend over time.
 2. Plots the BMI values on a graph with timestamps using Matplotlib.

### 5. Graphical User Interface (GUI):

 1. Provides an easy-to-use, full-screen interface using the Tkinter library.
 2. Offers additional theming options via ttkthemes.
 3. Allows users to enter their name, weight, and height to calculate BMI and view historical trends.

## How to Use
### 1. Calculate BMI:
       - Enter your name, weight (in kg), and height (in cm).
       - Click the "Calculate BMI" button to view your BMI result and category.
       - The data will be saved automatically to the database.
### 2. View User BMI History:
       - Click the "View All Users" button to see a list of users.
       - Select a user to visualize their BMI trend over time.

## Customization

  You can change the theme of the GUI by modifying the line
               
        root = ThemedTk(theme="arc")
  Replace "arc" with other theme options like "breeze", "equilux", etc.


  
