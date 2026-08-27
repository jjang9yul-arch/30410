import streamlit as st

st.set_page_config(
    page_title="F1 2026 시즌 공식 종합 뷰어",
    page_icon="🏎️",
    layout="wide"
)

# Custom CSS - F1 로고 확대, 빨간 줄 축소 및 레이아웃 밀림 현상 방지
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@600;800;900&family=Noto+Sans+KR:wght@400;700;900&display=swap');

    .stApp {
        background: linear-gradient(135deg, #090d16 0%, #121824 50%, #04060a 100%);
        color: #f3f4f6;
        font-family: 'Noto Sans KR', sans-serif;
    }

    /* 상단 헤더 컨테이너: 여백을 대폭 줄여 아래로 밀리는 현상 제거 */
    .f1-header-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        padding: 5px 0 15px 0;
        margin-bottom: 20px;
    }

    /* F1 로고 크기는 키우고 상하 여백 제거 */
    .f1-logo-img {
        width: 100%;
        max-width: 450px; 
        height: auto;
        object-fit: contain;
        filter: drop-shadow(0px 0px 20px rgba(225, 6, 0, 0.8));
        margin-bottom: 8px;
    }

    /* 기존의 두꺼운 빨간 줄을 얇고 세련된 악센트 라인으로 변경 */
    .f1-accent-line {
        width: 100%;
        max-width: 1200px;
        height: 2px;
        background: linear-gradient(90deg, transparent, #e10600, transparent);
    }

    /* 팀 및 프로필 카드 디자인 */
    .team-card {
        background: rgba(18, 24, 36, 0.9);
        border-radius: 12px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        padding: 20px;
        margin-bottom: 20px;
    }

    .team-title {
        font-family: 'Orbitron', sans-serif;
        font-size: 1.5rem;
        font-weight: 800;
    }

    .stat-badge {
        display: inline-block;
        background: rgba(225, 6, 0, 0.15);
        border: 1px solid rgba(225, 6, 0, 0.4);
        color: #ff4d4d;
        padding: 3px 10px;
        border-radius: 12px;
        font-size: 0.8rem;
        font-weight: 600;
        margin-right: 6px;
        margin-top: 6px;
    }

    .profile-card {
        background: #151b26;
        border-radius: 10px;
        border: 1px solid #2a3447;
        overflow: hidden;
        margin-bottom: 15px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
    }

    .profile-img-box {
        width: 100%;
        background-color: #0b0f17;
        display: flex;
        justify-content: center;
        align-items: center;
    }

    .profile-img-box img {
        width: 100%;
        height: 220px;
        object-fit: contain;
        padding: 8px;
    }

    .profile-info {
        padding: 12px;
        text-align: center;
        border-top: 1px solid rgba(255, 255, 255, 0.06);
    }

    .driver-num {
        font-family: 'Orbitron', sans-serif;
        color: #e10600;
        font-size: 1.2rem;
        font-weight: 900;
    }

    .driver-name {
        font-size: 1rem;
        font-weight: 700;
        color: #ffffff;
        margin: 3px 0;
    }
    </style>
""", unsafe_allow_html=True)

# 1. 상단 컴팩트 헤더 (F1 로고 확대 + 얇은 라인)
st.markdown("""
    <div class="f1-header-container">
        <img class="f1-logo-img" src="https://upload.wikimedia.org/wikipedia/commons/3/33/F1.svg" alt="F1 Logo">
        <div class="f1-accent-line"></div>
    </div>
""", unsafe_allow_html=True)

# 2026 시즌 공식 드라이버 순위 (총 22명)
driver_standings_2026 = [
    {"rank": 1, "driver": "키미 안토넬리 (Kimi Antonelli)", "team": "MER", "points": 242, "wins": 6},
    {"rank": 2, "driver": "조지 러셀 (George Russell)", "team": "MER", "points": 183, "wins": 2},
    {"rank": 3, "driver": "루이스 해밀턴 (Lewis Hamilton)", "team": "FER", "points": 183, "wins": 1},
    {"rank": 4, "driver": "랜도 노리스 (Lando Norris)", "team": "MCL", "points": 159, "wins": 2},
    {"rank": 5, "driver": "샤를 르클레르 (Charles Leclerc)", "team": "FER", "points": 155, "wins": 1},
    {"rank": 6, "driver": "막스 베르스타펜 (Max Verstappen)", "team": "RBR", "points": 112, "wins": 0},
    {"rank": 7, "driver": "오스카 피아스트리 (Oscar Piastri)", "team": "MCL", "points": 104, "wins": 0},
    {"rank": 8, "driver": "아이작 하자르 (Isack Hadjar)", "team": "RBC", "points": 68, "wins": 0},
    {"rank": 9, "driver": "리암 로슨 (Liam Lawson)", "team": "RBC", "points": 49, "wins": 0},
    {"rank": 10, "driver": "피에르 개슬리 (Pierre Gasly)", "team": "ALP", "points": 44, "wins": 0},
    {"rank": 11, "driver": "올리버 베어먼 (Oliver Bearman)", "team": "HAS", "points": 18, "wins": 0},
    {"rank": 12, "driver": "가브리에우 보르툴레투 (Gabriel Bortoleto)", "team": "SAU", "points": 10, "wins": 0},
    {"rank": 13, "driver": "니코 휠켄베르크 (Nico Hülkenberg)", "team": "SAU", "points": 6, "wins": 0},
    {"rank": 14, "driver": "카를로스 사인츠 (Carlos Sainz)", "team": "WIL", "points": 6, "wins": 0},
    {"rank": 15, "driver": "알렉산더 알본 (Alexander Albon)", "team": "WIL", "points": 5, "wins": 0},
    {"rank": 16, "driver": "에스테반 오콘 (Esteban Ocon)", "team": "HAS", "points": 3, "wins": 0},
    {"rank": 17, "driver": "페르난도 알론소 (Fernando Alonso)", "team": "AMR", "points": 3, "wins": 0},
    {"rank": 18, "driver": "츠노다 유키 (Yuki Tsunoda)", "team": "RBC", "points": 0, "wins": 0},
    {"rank": 19, "driver": "랜스 스트롤 (Lance Stroll)", "team": "AMR", "points": 0, "wins": 0},
    {"rank": 20, "driver": "발테리 보타스 (Valtteri Bottas)", "team": "CAD", "points": 0, "wins": 0},
    {"rank": 21, "driver": "세르히오 페레스 (Sergio Pérez)", "team": "CAD", "points": 0, "wins": 0},
    {"rank": 22, "driver": "잭 두한 (Jack Doohan)", "team": "ALP", "points": 0, "wins": 0}
]

# 2026 시즌 공식 팀 순위 (총 11개 팀)
team_standings_2026 = [
    {"rank": 1, "team": "MER (메르세데스)", "points": 425, "wins": 8},
    {"rank": 2, "team": "FER (페라리)", "points": 338, "wins": 2},
    {"rank": 3, "team": "MCL (맥라렌)", "points": 263, "wins": 2},
    {"rank": 4, "team": "RBR (레드불 레이싱)", "points": 186, "wins": 0},
    {"rank": 5, "team": "RBC (Racing Bulls / RB)", "points": 68, "wins": 0},
    {"rank": 6, "team": "ALP (알핀)", "points": 44, "wins": 0},
    {"rank": 7, "team": "HAS (하스)", "points": 21, "wins": 0},
    {"rank": 8, "team": "SAU (자우버 / 아우디)", "points": 16, "wins": 0},
    {"rank": 9, "team": "WIL (윌리엄스)", "points": 11, "wins": 0},
    {"rank": 10, "team": "AMR (애스턴 마틴)", "points": 3, "wins": 0},
    {"rank": 11, "team": "CAD (캐딜락 F1 팀)", "points": 0, "wins": 0}
]

# 11개 팀 전체 데이터베이스 (총 22명 드라이버 매칭)
f1_database = [
    {
        "team_en": "Mercedes-AMG Petronas F1 Team", "team_kr": "메르세데스", "color": "#27F4D2", "principal": "Toto Wolff", "power_unit": "Mercedes",
        "team_desc": "2026년 규정 변경에 완벽히 적응하여 챔피언십 선두를 질주하는 최강의 팀.",
        "drivers": [
            {"name_en": "Kimi Antonelli", "name_kr": "키미 안토넬리", "number": "12", "country": "이탈리아", "birth": "2006.08.25", "image_url": "https://media.formula1.com/d_driver_fallback_image.png/content/dam/fom-website/drivers/A/KIMANT01_Kimi_Antonelli/kimant01.png.transform/2col.png", "desc": "6승을 올리며 드라이버 챔피언십 1위 슈퍼 루키."},
            {"name_en": "George Russell", "name_kr": "조지 러셀", "number": "63", "country": "영국", "birth": "1998.02.15", "image_url": "https://media.formula1.com/d_driver_fallback_image.png/content/dam/fom-website/drivers/G/GEORUS01_George_Russell/georus01.png.transform/2col.png", "desc": "정교한 분석력과 꾸준한 포디움을 보여주는 에이스."}
        ]
    },
    {
        "team_en": "Scuderia Ferrari", "team_kr": "페라리", "color": "#E8002d", "principal": "Frédéric Vasseur", "power_unit": "Ferrari",
        "team_desc": "F1 역사 최다 우승에 도전하는 전설적인 이탈리아 명문 팀.",
        "drivers": [
            {"name_en": "Lewis Hamilton", "name_kr": "루이스 해밀턴", "number": "44", "country": "영국", "birth": "1985.01.07", "image_url": "https://media.formula1.com/d_driver_fallback_image.png/content/dam/fom-website/drivers/L/LEWHAM01_Lewis_Hamilton/lewham01.png.transform/2col.png", "desc": "페라리로 이적해 통산 8번째 월드 챔피언에 도전."},
            {"name_en": "Charles Leclerc", "name_kr": "샤를 르클레르", "number": "16", "country": "모나코", "birth": "1997.10.16", "image_url": "https://media.formula1.com/d_driver_fallback_image.png/content/dam/fom-website/drivers/C/CHALEC01_Charles_Leclerc/chalec01.png.transform/2col.png", "desc": "폭발적인 원랩 스피드를 자랑하는 모나코의 영웅."}
        ]
    },
    {
        "team_en": "McLaren Formula 1 Team", "team_kr": "맥라렌", "color": "#FF8000", "principal": "Andrea Stella", "power_unit": "Mercedes",
        "team_desc": "탁월한 샤시 설계로 상위권을 위협하는 전통의 강호.",
        "drivers": [
            {"name_en": "Lando Norris", "name_kr": "랜도 노리스", "number": "4", "country": "영국", "birth": "1999.11.13", "image_url": "https://media.formula1.com/d_driver_fallback_image.png/content/dam/fom-website/drivers/L/LANNOR01_Lando_Norris/lannor01.png.transform/2col.png", "desc": "화려한 추월쇼와 우승 다툼을 이끄는 에이스."},
            {"name_en": "Oscar Piastri", "name_kr": "오스카 피아스트리", "number": "81", "country": "호주", "birth": "2001.04.06", "image_url": "https://media.formula1.com/d_driver_fallback_image.png/content/dam/fom-website/drivers/O/OSCPIA01_Oscar_Piastri/oscpia01.png.transform/2col.png", "desc": "철두철미한 경기 운영을 선보이는 차세대 드라이버."}
        ]
    },
    {
        "team_en": "Oracle Red Bull Racing", "team_kr": "레드불 레이싱", "color": "#3671C6", "principal": "Christian Horner", "power_unit": "Red Bull Ford",
        "team_desc": "포드 파워유닛과 함께 새로운 도전에 나선 강팀.",
        "drivers": [
            {"name_en": "Max Verstappen", "name_kr": "막스 베르스타펜", "number": "1", "country": "네덜란드", "birth": "1997.09.30", "image_url": "https://media.formula1.com/d_driver_fallback_image.png/content/dam/fom-website/drivers/M/MAXVER01_Max_Verstappen/maxver01.png.transform/2col.png", "desc": "압도적 페이스와 공격적인 오버테이크의 챔피언."},
            {"name_en": "Yuki Tsunoda", "name_kr": "츠노다 유키", "number": "22", "country": "일본", "birth": "2000.05.11", "image_url": "https://media.formula1.com/d_driver_fallback_image.png/content/dam/fom-website/drivers/Y/YUKTSU01_Yuki_Tsunoda/yuktsu01.png.transform/2col.png", "desc": "과감한 브레이킹과 코너링 감각의 드라이버."}
        ]
    },
    {
        "team_en": "Cadillac F1 Team", "team_kr": "캐딜락 F1 팀", "color": "#FFD700", "principal": "Graeme Lowdon", "power_unit": "Ferrari",
        "team_desc": "2026년 F1에 새로 합류한 미국의 프리미엄 신생 창단 팀.",
        "drivers": [
            {"name_en": "Valtteri Bottas", "name_kr": "발테리 보타스", "number": "77", "country": "핀란드", "birth": "1989.08.28", "image_url": "https://media.formula1.com/d_driver_fallback_image.png/content/dam/fom-website/drivers/V/VALBOT01_Valtteri_Bottas/valbot01.png.transform/2col.png", "desc": "풍부한 노하우로 신생 팀의 차량 개발을 이끄는 베테랑."},
            {"name_en": "Sergio Pérez", "name_kr": "세르히오 페레스", "number": "11", "country": "멕시코", "birth": "1990.01.26", "image_url": "https://media.formula1.com/d_driver_fallback_image.png/content/dam/fom-website/drivers/S/SERPER01_Sergio_Perez/serper01.png.transform/2col.png", "desc": "탁월한 타이어 관리 능력을 가진 베테랑 드라이버."}
        ]
    }
]

# 탭 구성
tab1, tab2 = st.tabs(["🏆 2026 시즌 공식 순위 (22명/11팀)", "🏎️ 팀별 드라이버 프로필"])

with tab1:
    st.subheader("🏆 2026 FIA Formula 1 World Championship Standings")
    st.write("")

    col_r1, col_r2 = st.columns([1.2, 1])

    with col_r1:
        st.markdown("### **드라이버 순위 (22명)**")
        st.dataframe(
            driver_standings_2026,
            column_config={
                "rank": "순위",
                "driver": "드라이버 이름",
                "team": "소속 팀",
                "points": "포인트 (PTS)",
                "wins": "우승 횟수"
            },
            use_container_width=True,
            hide_index=True,
            height=780
        )

    with col_r2:
        st.markdown("### **컨스트럭터 순위 (11개 팀)**")
        st.dataframe(
            team_standings_2026,
            column_config={
                "rank": "순위",
                "team": "팀 명칭",
                "points": "총 포인트 (PTS)",
                "wins": "우승 횟수"
            },
            use_container_width=True,
            hide_index=True,
            height=460
        )

with tab2:
    team_names = [t["team_kr"] for t in f1_database]
    selected_team = st.selectbox("팀을 선택하세요", team_names)

    for team in f1_database:
        if team["team_kr"] == selected_team:
            st.markdown(f"""
                <div class="team-card" style="border-top: 4px solid {team['color']};">
                    <div class="team-title" style="color: {team['color']};">{team['team_en']} ({team['team_kr']})</div>
                    <div style="margin-top: 6px;">
                        <span class="stat-badge">감독: {team['principal']}</span>
                        <span class="stat-badge">엔진: {team['power_unit']}</span>
                    </div>
                </div>
            """, unsafe_allow_html=True)
            
            st.info(team["team_desc"])
            st.write("")
            st.subheader("소속 드라이버")
            
            cols = st.columns(len(team["drivers"]))
            for idx, driver in enumerate(team["drivers"]):
                with cols[idx]:
                    st.markdown(f"""
                        <div class="profile-card">
                            <div class="profile-img-box">
                                <img src="{driver['image_url']}" alt="{driver['name_kr']}">
                            </div>
                            <div class="profile-info">
                                <div class="driver-num">#{driver['number']}</div>
                                <div class="driver-name">{driver['name_kr']}</div>
                                <div style="font-size: 0.75rem; color: #8892b0;">{driver['name_en']}</div>
                                <div style="font-size: 0.75rem; color: #a0aec0; margin-top: 4px;">국적: {driver['country']}</div>
                                <div style="font-size: 0.8rem; color: #cbd5e0; margin-top: 6px;">{driver['desc']}</div>
                            </div>
                        </div>
                    """, unsafe_allow_html=True)
