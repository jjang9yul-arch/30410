import streamlit as st

st.set_page_config(
    page_title="F1 2026 시즌 대시보드",
    page_icon="🏎️",
    layout="wide"
)

# Custom CSS - 대형 F1 로고, 상단으로 당겨진 빨간 라인, 백과사전풍 설명 제거 및 하얀 글씨
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@600;800;900&family=Noto+Sans+KR:wght@400;700;900&display=swap');

    .stApp {
        background: linear-gradient(135deg, #07090f 0%, #11151f 50%, #030406 100%);
        color: #ffffff !important;
        font-family: 'Noto Sans KR', sans-serif;
    }

    /* 상단 헤더 컨테이너: 여백을 바짝 당겨 위로 배치 */
    .f1-header-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        padding: 5px 0 0 0;
        margin-bottom: 20px;
    }

    /* F1 로고 크게 복원 */
    .f1-logo-img {
        width: 100%;
        max-width: 550px;
        height: auto;
        object-fit: contain;
        filter: drop-shadow(0px 0px 22px rgba(225, 6, 0, 0.9));
        margin-bottom: 8px;
    }

    /* 빨간 줄을 로고 바로 밑으로 바짝 당겨서 얇게 배치 */
    .f1-accent-line {
        width: 100%;
        max-width: 1200px;
        height: 3px;
        background: linear-gradient(90deg, transparent, #e10600, transparent);
        margin-top: -2px;
    }

    /* 하얀 글씨 보장 */
    h1, h2, h3, h4, h5, h6, p, span, label, div {
        color: #ffffff !important;
    }

    /* 팀 카드 디자인 */
    .team-card {
        background: rgba(18, 23, 33, 0.9);
        border-radius: 12px;
        border: 1px solid rgba(255, 255, 255, 0.15);
        padding: 20px;
        margin-bottom: 20px;
        box-shadow: 0 6px 20px rgba(0, 0, 0, 0.4);
    }

    .team-title {
        font-family: 'Orbitron', sans-serif;
        font-size: 1.6rem;
        font-weight: 900;
    }

    .stat-badge {
        display: inline-block;
        background: rgba(225, 6, 0, 0.25);
        border: 1px solid rgba(225, 6, 0, 0.6);
        color: #ff6b6b !important;
        padding: 4px 12px;
        border-radius: 15px;
        font-size: 0.85rem;
        font-weight: 700;
        margin-right: 8px;
        margin-top: 8px;
    }

    /* 드라이버 프로필 카드 (백과사전식 장문 제거, 깔끔한 정보형) */
    .driver-card {
        background: #111622;
        border-radius: 10px;
        border: 1px solid #2a3447;
        padding: 15px;
        margin-bottom: 15px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.4);
    }

    .driver-num {
        font-family: 'Orbitron', sans-serif;
        color: #e10600 !important;
        font-size: 1.2rem;
        font-weight: 900;
    }

    .driver-name {
        font-size: 1.1rem;
        font-weight: 800;
        color: #ffffff !important;
        margin: 4px 0;
    }
    </style>
""", unsafe_allow_html=True)

# 1. 상단 대형 F1 로고 및 위로 당겨진 빨간 줄 헤더
st.markdown("""
    <div class="f1-header-container">
        <img class="f1-logo-img" src="https://upload.wikimedia.org/wikipedia/commons/3/33/F1.svg" alt="F1 Logo">
        <div class="f1-accent-line"></div>
    </div>
""", unsafe_allow_html=True)

# 2026 시즌 전체 11개 팀 및 22명 선수 데이터베이스
f1_teams_database = [
    {
        "team_en": "Mercedes-AMG Petronas F1 Team", "team_kr": "메르세데스", "color": "#27F4D2", "principal": "Toto Wolff", "power_unit": "Mercedes",
        "drivers": [
            {"name_en": "Kimi Antonelli", "name_kr": "키미 안토넬리", "number": "12", "country": "이탈리아 🇮🇹", "birth": "2006.08.25"},
            {"name_en": "George Russell", "name_kr": "조지 러셀", "number": "63", "country": "영국 🇬🇧", "birth": "1998.02.15"}
        ]
    },
    {
        "team_en": "Scuderia Ferrari", "team_kr": "페라리", "color": "#E8002d", "principal": "Frédéric Vasseur", "power_unit": "Ferrari",
        "drivers": [
            {"name_en": "Lewis Hamilton", "name_kr": "루이스 해밀턴", "number": "44", "country": "영국 🇬🇧", "birth": "1985.01.07"},
            {"name_en": "Charles Leclerc", "name_kr": "샤를 르클레르", "number": "16", "country": "모나코 🇲🇨", "birth": "1997.10.16"}
        ]
    },
    {
        "team_en": "McLaren Formula 1 Team", "team_kr": "맥라렌", "color": "#FF8000", "principal": "Andrea Stella", "power_unit": "Mercedes",
        "drivers": [
            {"name_en": "Lando Norris", "name_kr": "랜도 노리스", "number": "4", "country": "영국 🇬🇧", "birth": "1999.11.13"},
            {"name_en": "Oscar Piastri", "name_kr": "오스카 피아스트리", "number": "81", "country": "호주 🇦🇺", "birth": "2001.04.06"}
        ]
    },
    {
        "team_en": "Oracle Red Bull Racing", "team_kr": "레드불 레이싱", "color": "#3671C6", "principal": "Christian Horner", "power_unit": "Red Bull Ford",
        "drivers": [
            {"name_en": "Max Verstappen", "name_kr": "막스 베르스타펜", "number": "1", "country": "네덜란드 🇳🇱", "birth": "1997.09.30"},
            {"name_en": "Isack Hadjar", "name_kr": "아이작 하자르", "number": "6", "country": "프랑스 🇫🇷", "birth": "2004.09.28"}
        ]
    },
    {
        "team_en": "Visa Cash App Racing Bulls", "team_kr": "레이싱 불스 (RB)", "color": "#6692FF", "principal": "Laurent Mekies", "power_unit": "Red Bull Ford",
        "drivers": [
            {"name_en": "Liam Lawson", "name_kr": "리암 로슨", "number": "30", "country": "뉴질랜드 🇳🇿", "birth": "2002.02.11"},
            {"name_en": "Arvid Lindblad", "name_kr": "아르비드 린드블라드", "number": "41", "country": "영국 🇬🇧", "birth": "2007.08.08"}
        ]
    },
    {
        "team_en": "BWT Alpine F1 Team", "team_kr": "알핀", "color": "#FF87BC", "principal": "Oliver Oakes", "power_unit": "Mercedes",
        "drivers": [
            {"name_en": "Pierre Gasly", "name_kr": "피에르 개슬리", "number": "10", "country": "프랑스 🇫🇷", "birth": "1996.02.07"},
            {"name_en": "Franco Colapinto", "name_kr": "프랑코 콜라핀토", "number": "43", "country": "아르헨티나 🇦🇷", "birth": "2003.05.27"}
        ]
    },
    {
        "team_en": "TGR Haas F1 Team", "team_kr": "하스", "color": "#B6BABD", "principal": "Ayao Komatsu", "power_unit": "Ferrari",
        "drivers": [
            {"name_en": "Esteban Ocon", "name_kr": "에스테반 오콘", "number": "31", "country": "프랑스 🇫🇷", "birth": "1996.09.17"},
            {"name_en": "Oliver Bearman", "name_kr": "올리버 베어먼", "number": "87", "country": "영국 🇬🇧", "birth": "2005.05.08"}
        ]
    },
    {
        "team_en": "Audi F1 Team", "team_kr": "아우디 (자우버)", "color": "#00E785", "principal": "Mattia Binotto", "power_unit": "Audi",
        "drivers": [
            {"name_en": "Nico Hülkenberg", "name_kr": "니코 휠켄베르크", "number": "27", "country": "독일 🇩🇪", "birth": "1987.08.19"},
            {"name_en": "Gabriel Bortoleto", "name_kr": "가브리에우 보르툴레투", "number": "5", "country": "브라질 🇧🇷", "birth": "2004.10.14"}
        ]
    },
    {
        "team_en": "Atlassian Williams Racing", "team_kr": "윌리엄스", "color": "#64C4FF", "principal": "James Vowles", "power_unit": "Mercedes",
        "drivers": [
            {"name_en": "Carlos Sainz", "name_kr": "카를로스 사인츠", "number": "55", "country": "스페인 🇪🇸", "birth": "1994.09.01"},
            {"name_en": "Alexander Albon", "name_kr": "알렉산더 알본", "number": "23", "country": "태국 🇹🇭", "birth": "1996.03.23"}
        ]
    },
    {
        "team_en": "Aston Martin Aramco F1 Team", "team_kr": "애스턴 마틴", "color": "#229971", "principal": "Andy Cowell", "power_unit": "Honda",
        "drivers": [
            {"name_en": "Fernando Alonso", "name_kr": "페르난도 알론소", "number": "14", "country": "스페인 🇪🇸", "birth": "1981.07.29"},
            {"name_en": "Lance Stroll", "name_kr": "랜스 스트롤", "number": "18", "country": "캐나다 🇨🇦", "birth": "1998.10.29"}
        ]
    },
    {
        "team_en": "Cadillac F1 Team", "team_kr": "캐딜락 F1 팀", "color": "#FFD700", "principal": "Graeme Lowdon", "power_unit": "Ferrari",
        "drivers": [
            {"name_en": "Valtteri Bottas", "name_kr": "발테리 보타스", "number": "77", "country": "핀란드 🇫🇮", "birth": "1989.08.28"},
            {"name_en": "Sergio Pérez", "name_kr": "세르히오 페레스", "number": "11", "country": "멕시코 🇲🇽", "birth": "1990.01.26"}
        ]
    }
]

# 2026 그랑프리 일정 및 포디움 결과 데이터
f1_races_2026 = [
    {"round": "1R", "country": "🇦🇺 오스트레일리아", "circuit": "앨버트 파크 서킷", "date": "2026.03.08", "status": "완료", "podium": ["🥇 조지 러셀 (MER)", "🥈 키미 안토넬리 (MER)", "🥉 샤를 르클레르 (FER)"]},
    {"round": "2R", "country": "🇨🇳 중국", "circuit": "상하이 인터내셔널 서킷", "date": "2026.03.15", "status": "완료", "podium": ["🥇 키미 안토넬리 (MER)", "🥈 조지 러셀 (MER)", "🥉 루이스 해밀턴 (FER)"]},
    {"round": "3R", "country": "🇯🇵 일본", "circuit": "스즈카 서킷", "date": "2026.03.29", "status": "완료", "podium": ["🥇 키미 안토넬리 (MER)", "🥈 오스카 피아스트리 (MCL)", "🥉 샤를 르클레르 (FER)"]},
    {"round": "4R", "country": "🇺🇸 미국 (마이애미)", "circuit": "마이애미 오토드로름", "date": "2026.05.03", "status": "완료", "podium": ["🥇 키미 안토넬리 (MER)", "🥈 랜도 노리스 (MCL)", "🥉 오스카 피아스트리 (MCL)"]},
    {"round": "5R", "country": "🇨🇦 캐나다", "circuit": "서킷 질 빌뇌브", "date": "2026.05.24", "status": "완료", "podium": ["🥇 키미 안토넬리 (MER)", "🥈 루이스 해밀턴 (FER)", "🥉 막스 베르스타펜 (RBR)"]},
    {"round": "6R", "country": "🇲🇨 모나코", "circuit": "서킷 드 모나코", "date": "2026.06.07", "status": "완료", "podium": ["🥇 키미 안토넬리 (MER)", "🥈 루이스 해밀턴 (FER)", "🥉 피에르 개슬리 (ALP)"]},
    {"round": "7R", "country": "🇪🇸 스페인", "circuit": "바르셀로나-카탈루냐", "date": "2026.06.14", "status": "완료", "podium": ["🥇 루이스 해밀턴 (FER)", "🥈 조지 러셀 (MER)", "🥉 랜도 노리스 (MCL)"]},
    {"round": "8R", "country": "🇦🇹 오스트리아", "circuit": "레드불 링", "date": "2026.06.28", "status": "완료", "podium": ["🥇 조지 러셀 (MER)", "🥈 막스 베르스타펜 (RBR)", "🥉 키미 안토넬리 (MER)"]},
    {"round": "9R", "country": "🇬🇧 영국", "circuit": "실버스톤 서킷", "date": "2026.07.05", "status": "완료", "podium": ["🥇 샤를 르클레르 (FER)", "🥈 조지 러셀 (MER)", "🥉 루이스 해밀턴 (FER)"]},
    {"round": "10R", "country": "🇧🇪 벨기에", "circuit": "스파-프랑코샹 서킷", "date": "2026.07.19", "status": "완료", "podium": ["🥇 키미 안토넬리 (MER)", "🥈 샤를 르클레르 (FER)", "🥉 막스 베르스타펜 (RBR)"]},
    {"round": "11R", "country": "🇭🇺 헝가리", "circuit": "헝가로링", "date": "2026.07.26", "status": "완료", "podium": ["🥇 랜도 노리스 (MCL)", "🥈 막스 베르스타펜 (RBR)", "🥉 키미 안토넬리 (MER)"]},
    {"round": "12R", "country": "🇳🇱 네덜란드", "circuit": "잔트포르트 서킷", "date": "2026.08.23", "status": "완료", "podium": ["🥇 랜도 노리스 (MCL)", "🥈 키미 안토넬리 (MER)", "🥉 조지 러셀 (MER)"]},
    {"round": "13R", "country": "🇮🇹 이탈리아", "circuit": "몬차 서킷", "date": "2026.09.06", "status": "예정", "podium": []},
    {"round": "14R", "country": "🇪🇸 스페인 (마드리드)", "circuit": "마드리드 스트리트 서킷", "date": "2026.09.13", "status": "예정", "podium": []},
    {"round": "15R", "country": "🇦🇿 아제르바이잔", "circuit": "바쿠 시티 서킷", "date": "2026.09.26", "status": "예정", "podium": []},
    {"round": "16R", "country": "🇸🇬 싱가포르", "circuit": "마리나 베이 서킷", "date": "2026.10.11", "status": "예정", "podium": []},
    {"round": "17R", "country": "🇺🇸 미국 (오스틴)", "circuit": "COTA 서킷", "date": "2026.10.25", "status": "예정", "podium": []},
    {"round": "18R", "country": "🇲🇽 멕시코", "circuit": "로드리게스 서킷", "date": "2026.11.01", "status": "예정", "podium": []},
    {"round": "19R", "country": "🇧🇷 브라질", "circuit": "인터라고스 서킷", "date": "2026.11.08", "status": "예정", "podium": []},
    {"round": "20R", "country": "🇺🇸 미국 (라스베이거스)", "circuit": "라스베이거스 스트립", "date": "2026.11.21", "status": "예정", "podium": []},
    {"round": "21R", "country": "🇶🇦 카타르", "circuit": "루사일 서킷", "date": "2026.11.29", "status": "예정", "podium": []},
    {"round": "22R", "country": "🇦🇪 아랍에미리트", "circuit": "야스 마리나 서킷", "date": "2026.12.06", "status": "예정", "podium": []}
]

# 탭 메뉴 구성
tab1, tab2, tab3 = st.tabs(["🔍 F1 팀 검색 및 선수 정보", "🏎️ 2026 전체 11개 팀 라인업", "📅 2026 그랑프리 일정 & 포디움"])

# [탭 1] 팀 검색 및 소속 선수 확인
with tab1:
    st.subheader("🔍 F1 팀 및 소속 선수 검색")
    st.write("")
    
    team_name_list = [t["team_kr"] for t in f1_teams_database]
    selected_search_team = st.selectbox("검색할 팀 선택", team_name_list)
    
    for team in f1_teams_database:
        if team["team_kr"] == selected_search_team:
            st.markdown(f"""
                <div class="team-card" style="border-top: 5px solid {team['color']};">
                    <div class="team-title" style="color: {team['color']};">{team['team_en']} ({team['team_kr']})</div>
                    <div style="margin-top: 10px;">
                        <span class="stat-badge">감독: {team['principal']}</span>
                        <span class="stat-badge">파워 유닛: {team['power_unit']}</span>
                    </div>
                </div>
            """, unsafe_allow_html=True)
            
            st.markdown("### 👥 소속 드라이버 (국적 및 생년월일)")
            d_cols = st.columns(2)
            for idx, driver in enumerate(team["drivers"]):
                with d_cols[idx]:
                    st.markdown(f"""
                        <div class="driver-card">
                            <div class="driver-num">#{driver['number']}</div>
                            <div class="driver-name">{driver['name_kr']} ({driver['name_en']})</div>
                            <hr style="border-color: rgba(255,255,255,0.1); margin: 8px 0;">
                            <p style="margin: 4px 0;"><b>국적:</b> {driver['country']}</p>
                            <p style="margin: 4px 0;"><b>생년월일:</b> {driver['birth']}</p>
                        </div>
                    """, unsafe_allow_html=True)

# [탭 2] 2026 전체 11개 팀 및 22명 선수 리스트
with tab2:
    st.subheader("🏁 2026 시즌 전체 11개 팀 & 22명 드라이버")
    st.write("")

    for team in f1_teams_database:
        st.markdown(f"""
            <div class="team-card" style="border-left: 6px solid {team['color']};">
                <div class="team-title" style="color: {team['color']};">{team['team_en']} ({team['team_kr']})</div>
                <div style="margin-top: 8px;">
                    <span class="stat-badge">감독: {team['principal']}</span>
                    <span class="stat-badge">엔진: {team['power_unit']}</span>
                </div>
            </div>
        """, unsafe_allow_html=True)
        
        c_cols = st.columns(2)
        for i, driver in enumerate(team["drivers"]):
            with c_cols[i]:
                st.markdown(f"""
                    <div class="driver-card">
                        <div class="driver-num">#{driver['number']}</div>
                        <div class="driver-name">{driver['name_kr']} ({driver['name_en']})</div>
                        <p style="margin: 4px 0; font-size: 0.9rem;">국적: {driver['country']} | 생년월일: {driver['birth']}</p>
                    </div>
                """, unsafe_allow_html=True)
        st.write("---")

# [탭 3] 2026 그랑프리 일정표 및 포디움 결과
with tab3:
    st.subheader("📅 2026 FIA F1 월드 챔피언십 일정 & 포디움 결과")
    st.write("")

    for race in f1_races_2026:
        with st.container():
            col_info, col_podium = st.columns([1.2, 1.8])
            
            with col_info:
                st.markdown(f"### **{race['round']} - {race['country']}**")
                st.write(f"📍 **서킷:** {race['circuit']}")
                st.write(f"📅 **일정:** {race['date']}")
                st.write(f"📌 **상태:** {'✅ 경기 완료' if race['status'] == '완료' else '⏳ 레이스 예정'}")
            
            with col_podium:
                if race["status"] == "완료" and len(race["podium"]) > 0:
                    st.markdown("##### 🏆 **포디움 (TOP 3 결과)**")
                    for p in race["podium"]:
                        st.markdown(f"- {p}")
                else:
                    st.info("아직 진행되지 않은 다가오는 그랑프리 경기입니다.")
            
            st.markdown("---")
