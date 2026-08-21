import streamlit as st
import pandas as pd
import datetime

# Set page configuration
st.set_page_config(
    page_title="Tone & Trim Fitness Tracker",
    page_icon="💪",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Custom CSS for polished mobile styling
st.markdown("""
    <style>
    .main-header {
        background: linear-gradient(135deg, #0f172a 0%, #1e3a8a 100%);
        padding: 20px;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin-bottom: 20px;
    }
    .metric-card {
        background-color: #f8fafc;
        border: 1px solid #e2e8f0;
        border-radius: 8px;
        padding: 12px;
        text-align: center;
    }
    .stButton>button {
        width: 100%;
        background-color: #2563eb;
        color: white;
        font-weight: bold;
        border-radius: 8px;
        padding: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize Session State Data Store
if 'workout_logs' not in st.session_state:
    st.session_state.workout_logs = pd.DataFrame(
        columns=['Date', 'Day', 'Exercise', 'Set 1 (kg/reps)', 'Set 2 (kg/reps)', 'Set 3 (kg/reps)', 'Notes']
    )

if 'milestones' not in st.session_state:
    st.session_state.milestones = pd.DataFrame([
        {'Phase': 'Phase 1 (Wks 1-4)', 'Target Weight': '12.1 - 12.3 stone', 'Actual Weight': '', 'Date Logged': '', 'Notes': ''},
        {'Phase': 'Phase 2 (Wks 5-8)', 'Target Weight': '11.8 - 12.0 stone', 'Actual Weight': '', 'Date Logged': '', 'Notes': ''},
        {'Phase': 'Phase 3 (Wks 9-12)', 'Target Weight': '11.0 - 11.5 stone', 'Actual Weight': '', 'Date Logged': '', 'Notes': ''}
    ])

# Header
st.markdown("""
<div class="main-header">
    <h2 style="margin:0; color:white;">💪 Tone & Trim Mobile Tracker</h2>
    <p style="margin:5px 0 0 0; color:#93c5fd;">53 M | Target: 11.0 - 11.5 Stone</p>
</div>
""", unsafe_allow_html=True)

# App Navigation Tabs
tab1, tab2, tab3, tab4 = st.tabs(["🏋️ Log Workout", "📈 Log Milestones", "📊 History", "🥗 Plan Overview"])

# Exercise Graphic Links Mapping
exercise_graphics = {
    "Dumbbell Overhead Shoulder Press": "https://commons.wikimedia.org/wiki/File:Dumbbell-Overhead-Shoulder-Press.gif",
    "Lateral Raises (DB or Cable)": "https://commons.wikimedia.org/wiki/File:Side-Lateral-Raise.gif",
    "Incline DB Chest Press": "https://commons.wikimedia.org/wiki/File:Incline-Dumbbell-Press.gif",
    "Seated Cable Row / Pulldown": "https://commons.wikimedia.org/wiki/File:Seated-Cable-Row.gif",
    "Standing Bicep Curls": "https://commons.wikimedia.org/wiki/File:Dumbbell-Bicep-Curl.gif",
    "Triceps Rope Pushdowns": "https://commons.wikimedia.org/wiki/File:Triceps-Rope-Pushdown.gif",
    "Leg Press or Goblet Squat": "https://commons.wikimedia.org/wiki/File:Leg-Press.gif",
    "Romanian Deadlifts (RDL)": "https://commons.wikimedia.org/wiki/File:Barbell-Romanian-Deadlift.gif",
    "Lying / Seated Leg Curls": "https://commons.wikimedia.org/wiki/File:Lying-Leg-Curl.gif",
    "Captain's Chair Knee Raises": "https://commons.wikimedia.org/wiki/File:Hanging-Knee-Raise.gif",
    "Plank Hold": "https://commons.wikimedia.org/wiki/File:Plank.gif",
    "Incline Treadmill Walk": "https://commons.wikimedia.org/wiki/File:Treadmill-Walking.gif",
    "Dumbbell Arnold Press": "https://commons.wikimedia.org/wiki/File:Arnold-Press.gif",
    "Cable Face Pulls": "https://commons.wikimedia.org/wiki/File:Cable-Face-Pull.gif",
    "Dumbbell Hammer Curls": "https://commons.wikimedia.org/wiki/File:Hammer-Curl.gif",
    "Overhead DB Tricep Extension": "https://commons.wikimedia.org/wiki/File:Overhead-Triceps-Extension.gif",
    "Ab Cable / Machine Crunches": "https://commons.wikimedia.org/wiki/File:Cable-Crunch.gif",
    "Weighted Russian Twists": "https://commons.wikimedia.org/wiki/File:Russian-Twist.gif"
}

# Routine Mapping
workout_routines = {
    "Day 1: Upper Body Definition": [
        "Dumbbell Overhead Shoulder Press",
        "Lateral Raises (DB or Cable)",
        "Incline DB Chest Press",
        "Seated Cable Row / Pulldown",
        "Standing Bicep Curls",
        "Triceps Rope Pushdowns"
    ],
    "Day 2: Lower Body & Core": [
        "Leg Press or Goblet Squat",
        "Romanian Deadlifts (RDL)",
        "Lying / Seated Leg Curls",
        "Captain's Chair Knee Raises",
        "Plank Hold"
    ],
    "Day 3: Low-Impact Cardio": [
        "Incline Treadmill Walk"
    ],
    "Day 4: Sculpting (Shoulders, Arms, Abs)": [
        "Dumbbell Arnold Press",
        "Cable Face Pulls",
        "Dumbbell Hammer Curls",
        "Overhead DB Tricep Extension",
        "Ab Cable / Machine Crunches",
        "Weighted Russian Twists"
    ]
}

# TAB 1: WORKOUT LOGGING
with tab1:
    st.subheader("Log Today's Gym Session")
    
    log_date = st.date_input("Date", datetime.date.today())
    selected_day = st.selectbox("Select Workout Routine", list(workout_routines.keys()))
    
    st.markdown("---")
    
    exercises = workout_routines[selected_day]
    logged_data = []
    
    for ex in exercises:
        st.markdown(f"### **{ex}**")
        
        # Link to Graphic
        graphic_url = exercise_graphics.get(ex, "#")
        st.markdown(f"🖼️ **[View Exercise Form Guide & Graphic]({graphic_url})**")
        
        c1, c2, c3 = st.columns(3)
        with c1:
            s1 = st.text_input(f"Set 1 (e.g. 14kg x 10)", key=f"{ex}_s1")
        with c2:
            s2 = st.text_input(f"Set 2", key=f"{ex}_s2")
        with c3:
            s3 = st.text_input(f"Set 3", key=f"{ex}_s3")
            
        ex_notes = st.text_input(f"Notes / Form feel", key=f"{ex}_notes")
        st.markdown("<br>", unsafe_allow_html=True)
        
        logged_data.append({
            'Date': log_date.strftime("%Y-%m-%d"),
            'Day': selected_day,
            'Exercise': ex,
            'Set 1 (kg/reps)': s1,
            'Set 2 (kg/reps)': s2,
            'Set 3 (kg/reps)': s3,
            'Notes': ex_notes
        })
        
    if st.button("💾 Save Workout Session"):
        new_entries = pd.DataFrame(logged_data)
        st.session_state.workout_logs = pd.concat([st.session_state.workout_logs, new_entries], ignore_index=True)
        st.success("Session saved successfully!")

# TAB 2: MILESTONES
with tab2:
    st.subheader("Track Your 12-Week Milestones")
    
    for idx, row in st.session_state.milestones.iterrows():
        with st.expander(f"📍 {row['Phase']} (Target: {row['Target Weight']})", expanded=True):
            col1, col2 = st.columns(2)
            with col1:
                act_wt = st.text_input("Actual Weight (st/lbs)", value=row['Actual Weight'], key=f"wt_{idx}")
            with col2:
                dt_log = st.date_input("Date Measured", datetime.date.today(), key=f"dt_{idx}")
            
            notes = st.text_area("Body Definition & Waist Notes", value=row['Notes'], key=f"nt_{idx}")
            
            if st.button(f"Update {row['Phase']}", key=f"btn_{idx}"):
                st.session_state.milestones.at[idx, 'Actual Weight'] = act_wt
                st.session_state.milestones.at[idx, 'Date Logged'] = dt_log.strftime("%Y-%m-%d")
                st.session_state.milestones.at[idx, 'Notes'] = notes
                st.success(f"{row['Phase']} updated!")

# TAB 3: HISTORY & DATA
with tab3:
    st.subheader("Workout History & Logs")
    if st.session_state.workout_logs.empty:
        st.info("No workout logs saved yet. Start logging in Tab 1!")
    else:
        st.dataframe(st.session_state.workout_logs, use_container_width=True)
        
        csv = st.session_state.workout_logs.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="📥 Export Workout Logs as CSV",
            data=csv,
            file_name="tone_and_trim_workout_logs.csv",
            mime="text/csv"
        )

# TAB 4: PLAN OVERVIEW
with tab4:
    st.subheader("Nutrition & Goals Summary")
    st.markdown("""
    * **Daily Calories:** 1,650 – 1,750 kcal
    * **Daily Protein:** 140 – 160g
    * **Water Target:** 2.5 – 3.0 Liters
    * **Primary Focus:** Shoulder width, Arm shape, Upper abdominal definition.
    """)