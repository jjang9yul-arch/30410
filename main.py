import streamlit as st

# 1. 페이지 기본 설정
st.set_page_config(
    page_title="🏎️ F1 Hub App",
    page_icon="🏎️",
    layout="wide"
)

# 커스텀 다크 모드 스타일링
st.markdown("""
    <style>
    .main-title {
        color: #E10600;
        font-size: 2.8rem;
        font-weight: bold;
        text-align: center;
        margin-bottom: 25px;
    }
    .sub-title {
        color: #FFFFFF;
        border-bottom: 2px solid #E10600;
        padding-bottom: 8px;
        margin-bottom: 15px;
    }
    </style>
""", unsafe_allow_html=True)

# 2. 전체 F1 팀 데이터 (10개 공식 팀 및 검증된 이미지 URL)
F1_TEAMS = {
    "Red Bull": {
        "color": "#3671C6",
        "logo": "https://upload.wikimedia.org/wikipedia/en/c/c4/Red_Bull_Racing_logo.svg",
        "drivers": [
            {"name": "Max Verstappen", "no": "1", "country": "🇳🇱 Netherlands"},
            {"name": "Isack Hadjar", "no": "6", "country": "🇫🇷 France"}
        ]
    },
    "Ferrari": {
        "color": "#E80020",
        "logo": "https://upload.wikimedia.org/wikipedia/en/d/d1/Ferrari-Logo.svg",
        "drivers": [
            {"name": "Charles Leclerc", "no": "16", "country": "🇲🇨 Monaco"},
            {"name": "Lewis Hamilton", "no": "44", "country": "🇬🇧 United Kingdom"}
        ]
    },
    "McLaren": {
        "color": "#FF8000",
        "logo": "https://upload.wikimedia.org/wikipedia/en/6/66/McLaren_Racing_logo.svg",
        "drivers": [
            {"name": "Lando Norris", "no": "4", "country": "🇬🇧 United Kingdom"},
            {"name": "Oscar Piastri", "no": "81", "country": "🇦🇺 Australia"}
        ]
    },
    "Mercedes": {
        "color": "#27F4D2",
        "logo": "https://upload.wikimedia.org/wikipedia/commons/f/fb/Mercedes_AMG_Petronas_F1_Logo.svg",
        "drivers": [
            {"name": "George Russell", "no": "63", "country": "🇬🇧 United Kingdom"},
            {"name": "Andrea Kimi Antonelli", "no": "12", "country": "🇮🇹 Italy"}
        ]
    },
    "Aston Martin": {
        "color": "#229971",
        "logo": "https://upload.wikimedia.org/wikipedia/commons/5/53/Aston_Martin_logo.svg",
        "drivers": [
            {"name": "Fernando Alonso", "no": "14", "country": "🇪🇸 Spain"},
            {"name": "Lance Stroll", "no": "18", "country": "🇨🇦 Canada"}
        ]
    },
    "Alpine": {
        "color": "#0093CC",
        "logo": "https://upload.wikimedia.org/wikipedia/commons/7/7e/Alpine_F1_Team_Logo.svg",
        "drivers": [
            {"name": "Pierre Gasly", "no": "10", "country": "🇫🇷 France"},
            {"name": "Franco Colapinto", "no": "43", "country": "🇦🇷 Argentina"}
        ]
    },
    "Williams": {
        "color": "#64C4FF",
        "logo": "https://upload.wikimedia.org/wikipedia/commons/8/82/Williams_Racing_2020_Logo.svg",
        "drivers": [
            {"name": "Alexander Albon", "no": "23", "country": "🇹🇭 Thailand"},
            {"name": "Carlos Sainz", "no": "55", "country": "🇪🇸 Spain"}
        ]
    },
    "Haas": {
        "color": "#B6BABD",
        "logo": "https://upload.wikimedia.org/wikipedia/commons/d/d4/Haas_F1_Team_logo.svg",
        "drivers": [
            {"name": "Esteban Ocon", "no": "31", "country": "🇫🇷 France"},
            {"name": "Oliver Bearman", "no": "87", "country": "🇬🇧 United Kingdom"}
        ]
    },
    "Racing Bulls": {
        "color": "#6692FF",
        "logo": "https://upload.wikimedia.org/wikipedia/en/a/a2/Racing_Bulls_logo.svg",
        "drivers": [
            {"name": "Liam Lawson", "no": "30", "country": "🇳🇿 New Zealand"},
            {"name": "Arvid Lindblad", "no": "41", "country": "🇬🇧 United Kingdom"}
        ]
    },
    "Audi": {
        "color": "#C0C0C0",
        "logo": "https://upload.wikimedia.org/wikipedia/commons/9/92/Audi-Logo_2016.svg",
        "drivers": [
            {"name": "Nico Hülkenberg", "no": "27", "country": "🇩🇪 Germany"},
            {"name": "Gabriel Bortoleto", "no": "5", "country": "🇧🇷 Brazil"}
        ]
    }
}

# 3. 2026 F1 레이스 일정 데이터 (유지)
F1_SCHEDULE_2026 = [
    {"round": "R01", "gp": "🇦🇺 Australian GP", "circuit": "Albert Park", "date": "03.06 - 03.08"},
    {"round": "R02", "gp": "🇨🇳 Chinese GP", "circuit": "Shanghai Circuit", "date": "03.13 - 03.15"},
    {"round": "R03", "gp": "🇯🇵 Japanese GP", "circuit": "Suzuka Circuit", "date": "03.27 - 03.29"},
    {"round": "R04", "gp": "🇺🇸 Miami GP", "circuit": "Miami Autodrome", "date": "05.01 - 05.03"},
    {"round": "R05", "gp": "🇨🇦 Canadian GP", "circuit": "Circuit Gilles Villeneuve", "date": "05.22 - 05.24"},
    {"round": "R06", "gp": "🇲🇨 Monaco GP", "circuit": "Circuit de Monaco", "date": "06.05 - 06.07"},
    {"round": "R07", "gp": "🇪🇸 Barcelona GP", "circuit": "Circuit de Barcelona", "date": "06.12 - 06.14"},
    {"round": "R08", "gp": "🇦🇹 Austrian GP", "circuit": "Red Bull Ring", "date": "06.26 - 06.28"},
    {"round": "R09", "gp": "🇬🇧 British GP", "circuit": "Silverstone Circuit", "date": "07.03 - 07.05"},
    {"round": "R10", "gp": "🇧🇪 Belgian GP", "circuit": "Spa-Francorchamps", "date": "07.17 - 07.19"},
    {"round": "R11", "gp": "🇭🇺 Hungarian GP", "circuit": "Hungaroring", "date": "07.24 - 07.26"},
    {"round": "R12", "gp": "🇳🇱 Dutch GP", "circuit": "Circuit Zandvoort", "date": "08.21 - 08.23"},
    {"round": "R13", "gp": "🇮🇹 Italian GP", "circuit": "Monza Circuit", "date": "09.04 - 09.06"},
    {"round": "R14", "gp": "🇪🇸 Spanish GP (Madrid)", "circuit": "Madring", "date": "09.11 - 09.13"},
    {"round": "R15", "gp": "🇦🇿 Azerbaijan GP", "circuit": "Baku City Circuit", "date": "09.24 - 09.26"},
    {"round": "R16", "gp": "🇸🇬 Singapore GP", "circuit": "Marina Bay Circuit", "date": "10.09 - 10.11"},
    {"round": "R17", "gp": "🇺🇸 United States GP", "circuit": "COTA", "date": "10.23 - 10.25"},
    {"round": "R18", "gp": "🇲🇽 Mexico City GP", "circuit": "Autódromo Hermanos Rodríguez", "date": "10.30 - 11.01"},
    {"round": "R19", "gp": "🇧🇷 São Paulo GP", "circuit": "Interlagos", "date": "11.06 - 11.08"},
    {"round": "R20", "gp": "🇺🇸 Las Vegas GP", "circuit": "Las Vegas Strip", "date": "11.19 - 11.21"},
    {"round": "R21", "gp": "🇶🇦 Qatar GP", "circuit": "Lusail Circuit", "date": "11.27 - 11.29"},
    {"round": "R22", "gp": "🇦🇪 Abu Dhabi GP", "circuit": "Yas Marina Circuit", "date": "12.04 - 12.06"},
]

# 화면 상단 헤더
st.markdown('<div class="main-title">🏁 FORMULA 1 WORLD CHAMPIONSHIP 🏎️</div>', unsafe_allow_html=True)

# 탭 구성
tab1, tab2 = st.tabs(["🔍 팀 & 드라이버 검색", "📅 2026 레이스 일정표"])

# TAB 1: 전체 팀 검색
with tab1:
    st.markdown('<h3 class="sub-title">전체 팀 검색 및 상세 정보</h3>', unsafe_allow_html=True)
    
    selected_team = st.selectbox("검색하거나 확인하고 싶은 팀을 선택하세요:", list(F1_TEAMS.keys()))
    
    if selected_team:
        team_data = F1_TEAMS[selected_team]
        
        col1, col2 = st.columns([1, 2])
        
        with col1:
            st.image(team_data["logo"], width=230)
            
        with col2:
            st.subheader(f"🏎️ {selected_team}")
            st.write("---")
            st.markdown("### **소속 드라이버**")
            for driver in team_data["drivers"]:
                st.info(f"**Car No. {driver['no']}** | {driver['name']} ({driver['country']})")

# TAB 2: 레이스 일정표
with tab2:
    st.markdown('<h3 class="sub-title">2026 시즌 전체 일정</h3>', unsafe_allow_html=True)
    
    for i in range(0, len(F1_SCHEDULE_2026), 2):
        col_a, col_b = st.columns(2)
        
        with col_a:
            item = F1_SCHEDULE_2026[i]
            with st.expander(f"**[{item['round']}] {item['gp']}**", expanded=True):
                st.write(f"📍 서킷: {item['circuit']}")
                st.caption(f"🗓️ 날짜: {item['date']}")
                
        if i + 1 < len(F1_SCHEDULE_2026):
            with col_b:
                item = F1_SCHEDULE_2026[i+1]
                with st.expander(f"**[{item['round']}] {item['gp']}**", expanded=True):
                    st.write(f"📍 서킷: {item['circuit']}")
                    st.caption(f"🗓️ 날짜: {item['date']}")
