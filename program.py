import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

st.title('AHL Teams')

DIVISONS = ['Pacific', 'Central', 'North', 'Atlantic']

DIVISON_COLORS = { 
    DIVISONS[0]: '#5177bc',
    DIVISONS[1]: '#ffa500',
    DIVISONS[2]: '#51bc60',
    DIVISONS[3]: '#bc5177',
}

on = st.toggle('Update Alignment')

if on:
    pacific_division = 1
    central_division = 3
else:
    pacific_division = 0
    central_division = 1

df = pd.DataFrame(
    [
        # Pacific Division: #0000ff
        ['Abbotsford Cannucks', 49.03068, -122.286645, DIVISONS[0], DIVISON_COLORS.get(DIVISONS[0]), DIVISON_COLORS.get(DIVISONS[0])],
        ['Bakersfield Condors', 35.372296,-119.012967, DIVISONS[0], DIVISON_COLORS.get(DIVISONS[0]), DIVISON_COLORS.get(DIVISONS[0])],
        ['Calgary Wranglers', 51.037216, -114.052938, DIVISONS[0], DIVISON_COLORS.get(DIVISONS[0]), DIVISON_COLORS.get(DIVISONS[0])],
        ['Coachella Valley Firebirds', 33.720577, -116.215562, DIVISONS[0], DIVISON_COLORS.get(DIVISONS[0]), DIVISON_COLORS.get(DIVISONS[0])],
        ['Henderson Silver Knights', 36.026217, -115.146664, DIVISONS[0], DIVISON_COLORS.get(DIVISONS[0]), DIVISON_COLORS.get(DIVISONS[0])],
        ['Ontario Reign', 34.049245, -117.583898, DIVISONS[0], DIVISON_COLORS.get(DIVISONS[0]), DIVISON_COLORS.get(DIVISONS[0])],
        ['San Diego Gulls', 32.755488, -117.212289, DIVISONS[0], DIVISON_COLORS.get(DIVISONS[0]), DIVISON_COLORS.get(DIVISONS[0])],
        ['San Jose Barracuda', 37.332335, -121.901262, DIVISONS[0], DIVISON_COLORS.get(DIVISONS[0]), DIVISON_COLORS.get(DIVISONS[0])],

        ['Tucson Roadrunners', 32.222607, -110.974711, DIVISONS[pacific_division], DIVISON_COLORS.get(DIVISONS[pacific_division]), DIVISON_COLORS.get(DIVISONS[0])],
        ['Colorado Eagles', 40.434436, -104.995806, DIVISONS[pacific_division], DIVISON_COLORS.get(DIVISONS[pacific_division]), DIVISON_COLORS.get(DIVISONS[0])],

        # Central Division
        ['Chicago Wolves', 42.049984, -87.902534, DIVISONS[1], DIVISON_COLORS.get(DIVISONS[1]), DIVISON_COLORS.get(DIVISONS[1])],
        ['Iowa Wild', 41.591989, -93.620866, DIVISONS[1], DIVISON_COLORS.get(DIVISONS[1]), DIVISON_COLORS.get(DIVISONS[1])],
        ['Manitoba Moose', 49.892501, -97.143767, DIVISONS[1], DIVISON_COLORS.get(DIVISONS[1]), DIVISON_COLORS.get(DIVISONS[1])],
        ['Milwaukee Admirals', 43.043948, -87.916961, DIVISONS[1], DIVISON_COLORS.get(DIVISONS[1]), DIVISON_COLORS.get(DIVISONS[1])],
        ['Rockford IceHogs', 42.094276, -88.280630, DIVISONS[1], DIVISON_COLORS.get(DIVISONS[1]), DIVISON_COLORS.get(DIVISONS[1])],
        ['Texas Stars', 30.437297, -97.732262, DIVISONS[1], DIVISON_COLORS.get(DIVISONS[1]), DIVISON_COLORS.get(DIVISONS[1])],

        ['Grand Rapids Griffins', 42.959501, -85.664532, DIVISONS[central_division], DIVISON_COLORS.get(DIVISONS[central_division]), DIVISON_COLORS.get(DIVISONS[1])],

        # North Division
        ['Bridgeport Islanders', 41.177035, -73.187452, DIVISONS[2], DIVISON_COLORS.get(DIVISONS[2]), DIVISON_COLORS.get(DIVISONS[2])],
        ['Charlotte Checkers', 35.225144, -80.839236, DIVISONS[2], DIVISON_COLORS.get(DIVISONS[2]), DIVISON_COLORS.get(DIVISONS[2])],
        ['Hartford Wolf Pack', 41.763705, -72.674299, DIVISONS[2], DIVISON_COLORS.get(DIVISONS[2]), DIVISON_COLORS.get(DIVISONS[2])],
        ['Hershey Bears', 40.270504, -76.882459, DIVISONS[2], DIVISON_COLORS.get(DIVISONS[2]), DIVISON_COLORS.get(DIVISONS[2])],
        ['Lehigh Valley Phantoms', 40.601952, -75.470277, DIVISONS[2], DIVISON_COLORS.get(DIVISONS[2]), DIVISON_COLORS.get(DIVISONS[2])],
        ['Providence Bruins', 41.823989, -71.417035, DIVISONS[2], DIVISON_COLORS.get(DIVISONS[2]), DIVISON_COLORS.get(DIVISONS[2])],
        ['Springfield Thunderbirds', 42.099815, -72.579978, DIVISONS[2], DIVISON_COLORS.get(DIVISONS[2]), DIVISON_COLORS.get(DIVISONS[2])],
        ['Wilkes-Barre/Scranton Penguins', 41.269160, -75.887936, DIVISONS[2], DIVISON_COLORS.get(DIVISONS[2]), DIVISON_COLORS.get(DIVISONS[2])],


        # Atlantic Division
        ['Bellville Senators', 44.162758, -77.383231, DIVISONS[3], DIVISON_COLORS.get(DIVISONS[3]), DIVISON_COLORS.get(DIVISONS[3])],
        ['Cleveland Monsters', 41.496577, -81.688076, DIVISONS[3], DIVISON_COLORS.get(DIVISONS[3]), DIVISON_COLORS.get(DIVISONS[3])],
        ['Laval Rocket', 45.561642, -73.555493, DIVISONS[3], DIVISON_COLORS.get(DIVISONS[3]), DIVISON_COLORS.get(DIVISONS[3])],
        ['Rochester Americans', 43.152780, -77.615214, DIVISONS[3], DIVISON_COLORS.get(DIVISONS[3]), DIVISON_COLORS.get(DIVISONS[3])],
        ['Syracuse Crunch', 43.048122, -76.155029, DIVISONS[3], DIVISON_COLORS.get(DIVISONS[3]), DIVISON_COLORS.get(DIVISONS[3])],
        ['Toronto Marlies', 43.643466, -79.379099, DIVISONS[3], DIVISON_COLORS.get(DIVISONS[3]), DIVISON_COLORS.get(DIVISONS[3])],
        ['Utica Comets', 43.098525, -75.223224, DIVISONS[3], DIVISON_COLORS.get(DIVISONS[3]), DIVISON_COLORS.get(DIVISONS[3])],
     ],
    columns=['team','lat', 'lon','division', 'color', 'original_color'])

def highlight_team_name(team_name):
    color_lookup = df.set_index('team')['original_color'].to_dict()
    return f"color: {color_lookup.get(team_name, 'Color Not Found')}"

col1, col2, col3, col4 = st.columns(4)
columns = [col1, col2, col3, col4]
for i, division in enumerate(DIVISONS):
    with columns[i]:
        st.header(division)
        # Filter DataFrame based on division and select only the 'team' column
        filtered_data = df[df['division'] == division]['team']
        
        # Rename series for clarity (if needed, though this might not work as expected without assigning back)
        filtered_data.rename('Team Name', inplace=True)
        filtered_df = filtered_data.to_frame()

        # Correctly apply styling
        styles = [
            {'selector': 'th', 'props': [('width', '500px')]},  # For headers
            {'selector': '.col0', 'props': [('width', '500px')]},  # Specific column by index (e.g., first column)
            # Add more selectors for more columns as needed
        ]

        styled_df = filtered_df.reset_index(drop=True).style.map(highlight_team_name).hide(axis="index") #.set_table_styles(styles)

        # Convert styled DataFrame to HTML and hide index and headers
        html = styled_df.to_html()
        
        # Display HTML in Streamlit
        st.markdown(html, unsafe_allow_html=True)
if on:
    st.header('Map of AHL Teams Realigned')
else: 
    st.header('Map of AHL Teams')
st.map(df, latitude='lat', longitude='lon', color='color', zoom=3.5, size=20000)
