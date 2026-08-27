import streamlit as st

st.set_page_config(
    page_title="F1 2026 시즌 종합 정보 Vault",
    page_icon="🏎️",
    layout="wide"
)

# Custom CSS
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@600;800;900&family=Noto+Sans+KR:wght@400;700;900&display=swap');

    .stApp {
        background: linear-gradient(135deg, #0b0e14 0%, #151a24 50%, #05070a 100%);
        color: #f3f4f6;
        font-family: 'Noto Sans KR', sans-serif;
    }

    /* 컴팩트한 헤더 컨테이너 + 대형 로고 */
    .f1-header-container {
        display: flex;
        justify-content: center;
        align-items: center;
        padding: 20px 0; /* 컨테이너 높이는 슬림하게 유지 */
        border-bottom: 3px solid rgba(225, 6, 0, 0.6);
        margin-bottom: 30px;
    }

    .f1-logo-img {
        width: 850px; /* 로고 자체 크기 극대화 */
        max-width: 95%; 
        filter: drop-shadow(0px 0px 30px rgba(225, 6, 0, 0.9));
    }

    /* 팀 정보 카드 */
    .team-card {
        background: rgba(21, 26, 36, 0.85);
        border-radius: 12px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        padding: 20px;
        margin-bottom: 20px;
    }

    .team-title {
        font-family: 'Orbitron', sans-serif;
        font-size: 1.6rem;
        font-weight: 800;
    }

    .stat-badge {
        display: inline-block;
        background: rgba(225, 6, 0, 0.2);
        border: 1px solid rgba(225, 6, 0, 0.5);
        color: #ff4d4d;
        padding: 4px 12px;
        border-radius: 15px;
        font-size: 0.85rem;
        font-weight: 600;
        margin-right: 8px;
        margin-top: 8px;
    }

    /* 드라이버 프로필 카드 디자인 */
    .driver-card {
        background: #161b22;
        border-radius: 12px;
        border: 1px solid #30363d;
        overflow: hidden;
        text-align: center;
        margin-bottom: 20px;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.3);
    }

    .driver-img-box img {
        width: 100%;
        height: 260px;
        object-fit: cover;
        object-position: top;
        border-bottom: 2px solid rgba(225, 6, 0, 0.4);
    }

    .driver-info-box {
        padding: 15px;
    }

    .driver-number {
        font-family: 'Orbitron', sans-serif;
        color: #e10600;
        font-size: 1.2rem;
        font-weight: 900;
    }

    .driver-name {
        font-size: 1.15rem;
        font-weight: 700;
        margin: 5px 0;
        color: #ffffff;
    }

    .driver-sub {
        font-size: 0.85rem;
        color: #9ea7b3;
        margin-bottom: 8px;
    }
    </style>
""", unsafe_allow_html=True)

# 1. 헤더 영역 (로고 자체 크기 극대화)
st.markdown("""
    <div class="f1-header-container">
        <img class="f1-logo-img" src="https://upload.wikimedia.org/wikipedia/commons/3/33/F1.svg" alt="F1 Logo">
    </div>
""", unsafe_allow_html=True)

# 2026 시즌 22명 전체 드라이버 순위 데이터
driver_standings_2026 = [
    {"rank": 1, "driver": "키미 안토넬리", "team": "MER", "points": 242, "wins": 6},
    {"rank": 2, "driver": "조지 러셀", "team": "MER", "points": 215, "wins": 2},
    {"rank": 3, "driver": "랜도 노리스", "team": "MCL", "points": 188, "wins": 2},
    {"rank": 4, "driver": "샤를 르클레르", "team": "FER", "points": 164, "wins": 1},
    {"rank": 5, "driver": "루이스 해밀턴", "team": "FER", "points": 142, "wins": 1},
    {"rank": 6, "driver": "막스 베르스타펜", "team": "RBR", "points": 130, "wins": 0},
    {"rank": 7, "driver": "오스카 피아스트리", "team": "MCL", "points": 112, "wins": 0},
    {"rank": 8, "driver": "피에르 개슬리", "team": "ALP", "points": 64, "wins": 0},
    {"rank": 9, "driver": "츠노다 유키", "team": "RBR", "points": 48, "wins": 0},
    {"rank": 10, "driver": "알렉산더 알본", "team": "WIL", "points": 36, "wins": 0},
    {"rank": 11, "driver": "에스테반 오콘", "team": "HAS", "points": 28, "wins": 0},
    {"rank": 12, "driver": "니코 휠켄베르크", "team": "SAU", "points": 22, "wins": 0},
    {"rank": 13, "driver": "발테리 보타스", "team": "CAD", "points": 18, "wins": 0},
    {"rank": 14, "driver": "세르히오 페레스", "team": "CAD", "points": 12, "wins": 0},
    {"rank": 15, "driver": "올리버 베어만", "team": "HAS", "points": 10, "wins": 0},
    {"rank": 16, "driver": "아이작 하 자르", "team": "RBC", "points": 8, "wins": 0},
    {"rank": 17, "driver": "리암 로슨", "team": "RBC", "points": 6, "wins": 0},
    {"rank": 18, "driver": "카를로스 사인츠", "team": "WIL", "points": 4, "wins": 0},
    {"rank": 19, "driver": "잭 두한", "team": "ALP", "points": 2, "wins": 0},
    {"rank": 20, "driver": "가브리엘 보르톨레토", "team": "SAU", "points": 1, "wins": 0},
    {"rank": 21, "driver": "랜스 스트롤", "team": "AMR", "points": 0, "wins": 0},
    {"rank": 22, "driver": "페르난도 알론소", "team": "AMR", "points": 0, "wins": 0}
]

# 2026 시즌 11개 팀 전체 순위 데이터
team_standings_2026 = [
    {"rank": 1, "team": "MER (메르세데스)", "points": 457, "wins": 8},
    {"rank": 2, "team": "FER (페라리)", "points": 306, "wins": 2},
    {"rank": 3, "team": "MCL (맥라렌)", "points": 300, "wins": 2},
    {"rank": 4, "team": "RBR (레드불)", "points": 178, "wins": 0},
    {"rank": 5, "team": "ALP (알핀)", "points": 66, "wins": 0},
    {"rank": 6, "team": "WIL (윌리엄스)", "points": 40, "wins": 0},
    {"rank": 7, "team": "HAS (하스)", "points": 38, "wins": 0},
    {"rank": 8, "team": "CAD (캐딜락)", "points": 30, "wins": 0},
    {"rank": 9, "team": "SAU (자우버)", "points": 23, "wins": 0},
    {"rank": 10, "team": "RBC (RB)", "points": 14, "wins": 0},
    {"rank": 11, "team": "AMR (애스턴 마틴)", "points": 0, "wins": 0}
]

# 팀 상세 정보 및 이미지 링크 포함 데이터베이스
f1_database = [
    {
        "team_en": "McLaren Formula 1 Team", "team_kr": "맥라렌", "color": "#FF8000", "principal": "Andrea Stella", "power_unit": "Mercedes",
        "team_desc": "1963년 브루스 맥라렌이 창단한 전통의 명문 팀으로, F1 역사상 두 번째로 많은 컨스트럭터 우승 기록을 보유하고 있습니다.",
        "drivers": [
            {
                "name_en": "Lando Norris", "name_kr": "랜도 노리스", "number": "1", "country": "영국", "birth": "1999.11.13", "role": "메인 드라이버",
                "image_url": "https://media.formula1.com/d_driver_fallback_image.png/content/dam/fom-website/drivers/L/LANNOR01_Lando_Norris/lannor01.png.transform/2col.png",
                "desc": "정교한 퀄리파잉 스피드와 안정적인 레이스 페이스를 겸비한 리딩 드라이버입니다."
            },
            {
                "name_en": "Oscar Piastri", "name_kr": "오스카 피아스트리", "number": "81", "country": "호주", "birth": "2001.04.06", "role": "메인 드라이버",
                "image_url": "https://media.formula1.com/d_driver_fallback_image.png/content/dam/fom-website/drivers/O/OSCPIA01_Oscar_Piastri/oscpia01.png.transform/2col.png",
                "desc": "압박감이 심한 상황에서도 흔들리지 않는 냉정한 레이스 운영이 강점입니다."
            }
        ]
    },
    {
        "team_en": "Scuderia Ferrari", "team_kr": "페라리", "color": "#E8002d", "principal": "Frédéric Vasseur", "power_unit": "Ferrari",
        "team_desc": "1950년 F1 출범 이래 단 한 시즌도 빠짐없이 참가한 유일한 팀이자 모터스포츠의 상징입니다.",
        "drivers": [
            {
                "name_en": "Charles Leclerc", "name_kr": "샤를 르클레르", "number": "16", "country": "모나코", "birth": "1997.10.16", "role": "메인 드라이버",
                "image_url": "https://media.formula1.com/d_driver_fallback_image.png/content/dam/fom-website/drivers/C/CHALEC01_Charles_Leclerc/chalec01.png.transform/2col.png",
                "desc": "단 한 바퀴에 모든 것을 쏟아붓는 폭발적인 원랩 스피드가 최대 무기입니다."
            },
            {
                "name_en": "Lewis Hamilton", "name_kr": "루이스 해밀턴", "number": "44", "country": "영국", "birth": "1985.01.07", "role": "메인 드라이버",
                "image_url": "https://media.formula1.com/d_driver_fallback_image.png/content/dam/fom-website/drivers/L/LEWHAM01_Lewis_Hamilton/lewham01.png.transform/2col.png",
                "desc": "F1 통산 7회 월드 챔피언 기록을 보유한 살아있는 전설입니다."
            }
        ]
    },
    {
        "team_en": "Mercedes-AMG Petronas F1 Team", "team_kr": "메르세데스", "color": "#27F4D2", "principal": "Toto Wolff", "power_unit": "Mercedes",
        "team_desc": "독보적인 엔진 파워유닛 기술력과 정교한 데이터 분석을 바탕으로 언제나 강력한 전력을 보여줍니다.",
        "drivers": [
            {
                "name_en": "George Russell", "name_kr": "조지 러셀", "number": "63", "country": "영국", "birth": "1998.02.15", "role": "메인 드라이버",
                "image_url": "https://media.formula1.com/d_driver_fallback_image.png/content/dam/fom-website/drivers/G/GEORUS01_George_Russell/georus01.png.transform/2col.png",
                "desc": "어려운 조건 속에서도 꾸준히 포인트를 획득하는 높은 집중력을 자랑합니다."
            },
            {
                "name_en": "Kimi Antonelli", "name_kr": "키미 안토넬리", "number": "12", "country": "이탈리아", "birth": "2006.08.25", "role": "메인 드라이버",
                "image_url": "https://media.formula1.com/d_driver_fallback_image.png/content/dam/fom-website/drivers/A/KIMANT01_Kimi_Antonelli/kimant01.png.transform/2col.png",
                "desc": "엄청난 코너링 스피드로 2026 시즌 연승을 이끌고 있는 슈퍼 루키입니다."
            }
        ]
    },
    {
        "team_en": "Oracle Red Bull Racing", "team_kr": "레드불", "color": "#3671C6", "principal": "Christian Horner", "power_unit": "Honda RBPT",
        "team_desc": "압도적인 피트스탑 속도와 한계에 도전하는 공격적인 전략을 펼치는 팀입니다.",
        "drivers": [
            {
                "name_en": "Max Verstappen", "name_kr": "막스 베르스타펜", "number": "1", "country": "네덜란드", "birth": "1997.09.30", "role": "메인 드라이버",
                "image_url": "https://media.formula1.com/d_driver_fallback_image.png/content/dam/fom-website/drivers/M/MAXVER01_Max_Verstappen/maxver01.png.transform/2col.png",
                "desc": "타협 없는 공격적인 추월 방식과 압도적인 페이스를 보유한 챔피언입니다."
            },
            {
                "name_en": "Yuki Tsunoda", "name_kr": "츠노다 유키", "number": "22", "country": "일본", "birth": "2000.05.11", "role": "메인 드라이버",
                "image_url": "https://media.formula1.com/d_driver_fallback_image.png/content/dam/fom-website/drivers/Y/YUKTSU01_Yuki_Tsunoda/yuktsu01.png.transform/2col.png",
                "desc": "과감한 브레이킹 테크닉과 뛰어난 코너 추월 능력이 강점입니다."
            }
        ]
    },
    {
        "team_en": "Cadillac F1 Team", "team_kr": "캐딜락", "color": "#FFD700", "principal": "Graeme Lowdon", "power_unit": "Ferrari",
        "team_desc": "2026년 규정 개정에 맞춰 F1에 새롭게 출사표를 던진 GM의 창단 팀입니다.",
        "drivers": [
            {
                "name_en": "Valtteri Bottas", "name_kr": "발테리 보타스", "number": "77", "country": "핀란드", "birth": "1989.08.28", "role": "메인 드라이버",
                "image_url": "https://media.formula1.com/d_driver_fallback_image.png/content/dam/fom-website/drivers/V/VALBOT01_Valtteri_Bottas/valbot01.png.transform/2col.png",
                "desc": "통산 10회 우승 경험을 갖춘 베테랑으로 팀 개발을 이끌고 있습니다."
            },
            {
                "name_en": "Sergio Pérez", "name_kr": "세르히오 페레스", "number": "11", "country": "멕시코", "birth": "1990.01.26", "role": "메인 드라이버",
                "image_url": "https://media.formula1.com/d_driver_fallback_image.png/content/dam/fom-website/drivers/S/SERPER01_Sergio_Perez/serper01.png.transform/2col.png",
                "desc": "독보적인 타이어 관리 능력과 탁월한 위기관리 능력을 자랑합니다."
            }
        ]
    }
]

# 경기 일정 데이터
f1_races_2026 = [
    {"round": "1R", "country": "🇦🇺 오스트레일리아", "circuit": "앨버트 파크 서킷", "date": "2026. 03. 08", "status": "완료", "podium": {"1st": "🥇 조지 러셀 (MER)", "2nd": "🥈 키미 안토넬리 (MER)", "3rd": "🥉 샤를 르클레르 (FER)"}},
    {"round": "2R", "country": "🇨🇳 중국", "circuit": "상하이 인터내셔널 서킷", "date": "2026. 03. 15", "status": "완료", "podium": {"1st": "🥇 키미 안토넬리 (MER)", "2nd": "🥈 조지 러셀 (MER)", "3rd": "🥉 루이스 해밀턴 (FER)"}},
    {"round": "3R", "country": "🇯🇵 일본", "circuit": "스즈카 서킷", "date": "2026. 03. 29", "status": "완료", "podium": {"1st": "🥇 키미 안토넬리 (MER)", "2nd": "🥈 오스카 피아스트리 (MCL)", "3rd": "🥉 샤를 르클레르 (FER)"}},
    {"round": "4R", "country": "🇺🇸 미국 (마이애미)", "circuit": "마이애미 오토드로름", "date": "2026. 05. 03", "status": "완료", "podium": {"1st": "🥇 키미 안토넬리 (MER)", "2nd": "🥈 랜도 노리스 (MCL)", "3rd": "🥉 오스카 피아스트리 (MCL)"}},
    {"round": "5R", "country": "🇨🇦 캐나다", "circuit": "서킷 질 빌뇌브", "date": "2026. 05. 24", "status": "완료", "podium": {"1st": "🥇 키미 안토넬리 (MER)", "2nd": "🥈 루이스 해밀턴 (FER)", "3rd": "🥉 막스 베르스타펜 (RBR)"}},
    {"round": "6R", "country": "🇲🇨 모나코", "circuit": "서킷 드 모나코", "date": "2026. 06. 07", "status": "완료", "podium": {"1st": "🥇 키미 안토넬리 (MER)", "2nd": "🥈 루이스 해밀턴 (FER)", "3rd": "🥉 피에르 개슬리 (ALP)"}},
    {"round": "7R", "country": "🇪🇸 스페인", "circuit": "서킷 드 바르셀로나-카탈루냐", "date": "2026. 06. 14", "status": "완료", "podium": {"1st": "🥇 루이스 해밀턴 (FER)", "2nd": "🥈 조지 러셀 (MER)", "3rd": "🥉 랜도 노리스 (MCL)"}},
    {"round": "8R", "country": "🇦🇹 오스트리아", "circuit": "레드불 링", "date": "2026. 06. 28", "status": "완료", "podium": {"1st": "🥇 조지 러셀 (MER)", "2nd": "🥈 막스 베르스타펜 (RBR)", "3rd": "🥉 키미 안토넬리 (MER)"}},
    {"round": "9R", "country": "🇬🇧 영국", "circuit": "실버스톤 서킷", "date": "2026. 07. 05", "status": "완료", "podium": {"1st": "🥇 샤를 르클레르 (FER)", "2nd": "🥈 조지 러셀 (MER)", "3rd": "🥉 루이스 해밀턴 (FER)"}},
    {"round": "10R", "country": "🇧🇪 벨기에", "circuit": "스파-프랑코샹 서킷", "date": "2026. 07. 19", "status": "완료", "podium": {"1st": "🥇 키미 안토넬리 (MER)", "2nd": "🥈 샤를 르클레르 (FER)", "3rd": "🥉 막스 베르스타펜 (RBR)"}},
    {"round": "11R", "country": "🇭🇺 헝가리", "circuit": "헝가로링", "date": "2026. 07. 26", "status": "완료", "podium": {"1st": "🥇 랜도 노리스 (MCL)", "2nd": "🥈 막스 베르스타펜 (RBR)", "3rd": "🥉 키미 안토넬리 (MER)"}},
    {"round": "12R", "country": "🇳🇱 네덜란드", "circuit": "잔트포르트 서킷", "date": "2026. 08. 23", "status": "완료", "podium": {"1st": "🥇 랜도 노리스 (MCL)", "2nd": "🥈 키미 안토넬리 (MER)", "3rd": "🥉 조지 러셀 (MER)"}},
    {"round": "13R", "country": "🇮🇹 이탈리아", "circuit": "오토드로모 나치오날레 몬차", "date": "2026. 09. 06", "status": "예정", "podium": None},
    {"round": "14R", "country": "🇪🇸 스페인 (마드리드)", "circuit": "마드리드 스트리트 서킷", "date": "2026. 09. 13", "status": "예정", "podium": None},
    {"round": "15R", "country": "🇦🇿 아제르바이잔", "circuit": "바쿠 시티 서킷", "date": "2026. 09. 26", "status": "예정", "podium": None},
    {"round": "16R", "country": "🇸🇬 싱가포르", "circuit": "마리나 베이 스트리트 서킷", "date": "2026. 10. 11", "status": "예정", "podium": None},
    {"round": "17R", "country": "🇺🇸 미국 (오스틴)", "circuit": "서킷 오브 디 아메리카스", "date": "2026. 10. 25", "status": "예정", "podium": None},
    {"round": "18R", "country": "🇲🇽 멕시코", "circuit": "오토드로모 에르마노스 로드리게스", "date": "2026. 11. 01", "status": "예정", "podium": None},
    {"round": "19R", "country": "🇧🇷 브라질", "circuit": "호세 카를로스 파체 서킷 (인터라고스)", "date": "2026. 11. 08", "status": "예정", "podium": None},
    {"round": "20R", "country": "🇺🇸 미국 (베이거스)", "circuit": "라스베이거스 스트립 서킷", "date": "2026. 11. 21", "status": "예정", "podium": None},
    {"round": "21R", "country": "🇶🇦 카타르", "circuit": "루사일 인터내셔널 서킷", "date": "2026. 11. 29", "status": "예정", "podium": None},
    {"round": "22R", "country": "🇦🇪 아랍에미리트", "circuit": "야스 마리나 서킷", "date": "2026. 12. 06", "status": "예정", "podium": None}
]

# 탭 구성
tab1, tab2, tab3 = st.tabs(["🏆 2026 시즌 순위", "🏎️ F1 팀 & 드라이버", "📅 경기 일정 및 포디움"])

# Tab 1: 전체 순위
with tab1:
    st.subheader("🏆 2026 World Championship Standings")
    st.caption("12R 네덜란드 그랑프리 종료 기준 전체 22명 드라이버 및 11개 팀 순위입니다.")
    st.write("")

    col_rank1, col_rank2 = st.columns(2)

    with col_rank1:
        st.markdown("### 🏎️ **드라이버 순위 (22명 전체)**")
        st.dataframe(
            driver_standings_2026,
            column_config={
                "rank": "순위",
                "driver": "드라이버",
                "team": "팀 (TEAM)",
                "points": "포인트 (PTS)",
                "wins": "우승"
            },
            use_container_width=True,
            hide_index=True,
            height=810
        )

    with col_rank2:
        st.markdown("### 🛠️ **컨스트럭터(팀) 순위**")
        st.dataframe(
            team_standings_2026,
            column_config={
                "rank": "순위",
                "team": "팀 명칭",
                "points": "총 포인트 (PTS)",
                "wins": "우승"
            },
            use_container_width=True,
            hide_index=True,
            height=430
        )

# Tab 2: 팀 & 드라이버 프로필 (사진 카드 포함)
with tab2:
    team_names = [t["team_kr"] for t in f1_database]
    selected_team_name = st.selectbox("팀을 선택하세요", team_names)

    for team in f1_database:
        if team["team_kr"] == selected_team_name:
            st.markdown(f"""
                <div class="team-card" style="border-top: 5px solid {team['color']};">
                    <div class="team-title" style="color: {team['color']};">{team['team_en']} ({team['team_kr']})</div>
                    <div style="margin-top: 5px;">
                        <span class="stat-badge">팀 감독: {team['principal']}</span>
                        <span class="stat-badge">파워 유닛: {team['power_unit']}</span>
                    </div>
                </div>
            """, unsafe_allow_html=True)
            
            with st.expander(f"📖 {team['team_kr']} 팀 소개글 보기", expanded=True):
                st.write(team["team_desc"])
            
            st.write("")
            st.subheader("🏎️ 소속 드라이버 프로필")
            
            cols = st.columns(len(team["drivers"]))
            for idx, driver in enumerate(team["drivers"]):
                with cols[idx]:
                    # 프로필 이미지 카드
                    st.markdown(f"""
                        <div class="driver-card">
                            <div class="driver-img-box">
                                <img src="{driver['image_url']}" alt="{driver['name_kr']}">
                            </div>
                            <div class="driver-info-box">
                                <div class="driver-number">#{driver['number']}</div>
                                <div class="driver-name">{driver['name_kr']}</div>
                                <div class="driver-sub">{driver['name_en']}</div>
                                <div style="font-size:0.8rem; color:#8b949e;"><b>국적:</b> {driver['country']} | <b>생년월일:</b> {driver['birth']}</div>
                            </div>
                        </div>
                    """, unsafe_allow_html=True)
                    
                    with st.popover(f"🏎️ #{driver['number']} 상세 설명 보기", use_container_width=True):
                        st.markdown(f"#### #{driver['number']} {driver['name_kr']}")
                        st.divider()
                        st.write(f"• {driver['desc']}")

# Tab 3: 일정 및 포디움
with tab3:
    st.subheader("🏁 2026 FIA F1 그랑프리 일정 & 경기 결과")
    st.caption("라운드별 일정과 12R까지의 실제 TOP 3 포디움 결과입니다.")
    st.write("")

    for race in f1_races_2026:
        with st.container():
            col1, col2 = st.columns([1.2, 1.8])
            
            with col1:
                st.markdown(f"### **{race['round']} - {race['country']}**")
                st.write(f"📍 **서킷:** {race['circuit']}")
                st.write(f"📅 **결승일:** {race['date']}")
            
            with col2:
                if race["status"] == "완료" and race["podium"]:
                    st.markdown("##### 🏆 **포디움 (TOP 3)**")
                    st.write(f"{race['podium']['1st']}")
                    st.write(f"{race['podium']['2nd']}")
                    st.write(f"{race['podium']['3rd']}")
                else:
                    st.info("⏳ 경기 예정 (결과 미정)")
            
            st.divider()
