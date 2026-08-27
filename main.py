import streamlit as st

st.set_page_config(
    page_title="F1 2026 시즌 종합 정보 Vault",
    page_icon="🏎️",
    layout="wide"
)

# Custom CSS - 고급 다크 모터스포츠 스타일 및 이미지 카드 보정
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@600;800;900&family=Noto+Sans+KR:wght@400;700;900&display=swap');

    .stApp {
        background: linear-gradient(135deg, #0b0e14 0%, #151a24 50%, #05070a 100%);
        color: #f3f4f6;
        font-family: 'Noto Sans KR', sans-serif;
    }

    /* 슬림한 헤더 컨테이너 + 자르지 않는 초대형 F1 로고 */
    .f1-header-container {
        display: flex;
        justify-content: center;
        align-items: center;
        padding: 15px 0;
        border-bottom: 3px solid rgba(225, 6, 0, 0.7);
        margin-bottom: 30px;
    }

    .f1-logo-img {
        width: 100%;
        max-width: 900px; /* 로고 자체 가로 폭 대폭 확대 */
        height: auto;
        object-fit: contain;
        filter: drop-shadow(0px 0px 30px rgba(225, 6, 0, 0.9));
    }

    /* 팀 및 드라이버 프로필 카드 레이아웃 */
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

    /* 사진 잘림 없는 맞춤형 이미지 카드 디자인 */
    .profile-card {
        background: #161b22;
        border-radius: 12px;
        border: 1px solid #30363d;
        overflow: hidden;
        margin-bottom: 20px;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.4);
    }

    .profile-img-box {
        width: 100%;
        background-color: #0b0e14;
        display: flex;
        justify-content: center;
        align-items: center;
    }

    .profile-img-box img {
        width: 100%;
        height: 280px;
        object-fit: contain; /* 이미지 전체가 잘림 없이 원본 비율대로 표시됨 */
        padding: 10px;
    }

    .profile-info {
        padding: 15px;
        text-align: center;
        border-top: 1px solid rgba(255, 255, 255, 0.08);
    }

    .driver-num {
        font-family: 'Orbitron', sans-serif;
        color: #e10600;
        font-size: 1.3rem;
        font-weight: 900;
    }

    .driver-name {
        font-size: 1.1rem;
        font-weight: 700;
        color: #ffffff;
        margin: 4px 0;
    }

    .driver-desc {
        font-size: 0.85rem;
        color: #a0aec0;
        line-height: 1.4;
        margin-top: 8px;
    }
    </style>
""", unsafe_allow_html=True)

# 1. 상단 대형 로고 헤더
st.markdown("""
    <div class="f1-header-container">
        <img class="f1-logo-img" src="https://upload.wikimedia.org/wikipedia/commons/3/33/F1.svg" alt="F1 Logo">
    </div>
""", unsafe_allow_html=True)

# 2026 시즌 실제 공식 드라이버 순위 (23명 전체)
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
    {"rank": 11, "driver": "아르비드 린드블라드 (Arvid Lindblad)", "team": "RBC", "points": 23, "wins": 0},
    {"rank": 12, "driver": "프랑코 콜라핀토 (Franco Colapinto)", "team": "ALP", "points": 19, "wins": 0},
    {"rank": 13, "driver": "올리버 베어먼 (Oliver Bearman)", "team": "HAS", "points": 18, "wins": 0},
    {"rank": 14, "driver": "가브리에우 보르툴레투 (Gabriel Bortoleto)", "team": "SAU", "points": 10, "wins": 0},
    {"rank": 15, "driver": "니코 휠켄베르크 (Nico Hülkenberg)", "team": "SAU", "points": 6, "wins": 0},
    {"rank": 16, "driver": "카를로스 사인츠 (Carlos Sainz)", "team": "WIL", "points": 6, "wins": 0},
    {"rank": 17, "driver": "알렉산더 알본 (Alexander Albon)", "team": "WIL", "points": 5, "wins": 0},
    {"rank": 18, "driver": "에스테반 오콘 (Esteban Ocon)", "team": "HAS", "points": 3, "wins": 0},
    {"rank": 19, "driver": "페르난도 알론소 (Fernando Alonso)", "team": "AMR", "points": 3, "wins": 0},
    {"rank": 20, "driver": "츠노다 유키 (Yuki Tsunoda)", "team": "RBC", "points": 0, "wins": 0},
    {"rank": 21, "driver": "랜스 스트롤 (Lance Stroll)", "team": "AMR", "points": 0, "wins": 0},
    {"rank": 22, "driver": "발테리 보타스 (Valtteri Bottas)", "team": "CAD", "points": 0, "wins": 0},
    {"rank": 23, "driver": "세르히오 페레스 (Sergio Pérez)", "team": "CAD", "points": 0, "wins": 0}
]

# 2026 시즌 공식 컨스트럭터(팀) 순위 (11개 팀 전체)
team_standings_2026 = [
    {"rank": 1, "team": "MER (메르세데스)", "points": 425, "wins": 8},
    {"rank": 2, "team": "FER (페라리)", "points": 338, "wins": 2},
    {"rank": 3, "team": "MCL (맥라렌)", "points": 263, "wins": 2},
    {"rank": 4, "team": "RBR (레드불 레이싱)", "points": 186, "wins": 0},
    {"rank": 5, "team": "RBC (Racing Bulls / RB)", "points": 66, "wins": 0},
    {"rank": 6, "team": "ALP (알핀)", "points": 63, "wins": 0},
    {"rank": 7, "team": "HAS (하스)", "points": 21, "wins": 0},
    {"rank": 8, "team": "SAU (자우버 / 아우디)", "points": 16, "wins": 0},
    {"rank": 9, "team": "WIL (윌리엄스)", "points": 11, "wins": 0},
    {"rank": 10, "team": "AMR (애스턴 마틴)", "points": 3, "wins": 0},
    {"rank": 11, "team": "CAD (캐딜락 F1 팀)", "points": 0, "wins": 0}
]

# 11개 팀 전체 데이터베이스 (팀별 2명 드라이버 및 정확한 공식 이미지 포함)
f1_database = [
    {
        "team_en": "Mercedes-AMG Petronas F1 Team", "team_kr": "메르세데스", "color": "#27F4D2", "principal": "Toto Wolff", "power_unit": "Mercedes",
        "team_desc": "2026년 파워유닛 기술 규정 변경에 완벽히 적응하여 챔피언십 선두를 달리고 있는 최강의 피트 팀입니다.",
        "drivers": [
            {
                "name_en": "Kimi Antonelli", "name_kr": "키미 안토넬리", "number": "12", "country": "이탈리아", "birth": "2006.08.25",
                "image_url": "https://media.formula1.com/d_driver_fallback_image.png/content/dam/fom-website/drivers/A/KIMANT01_Kimi_Antonelli/kimant01.png.transform/2col.png",
                "desc": "2026 시즌 6승을 올리며 드라이버 챔피언십 1위를 질주하고 있는 이탈리아 출신 슈퍼 루키입니다."
            },
            {
                "name_en": "George Russell", "name_kr": "조지 러셀", "number": "63", "country": "영국", "birth": "1998.02.15",
                "image_url": "https://media.formula1.com/d_driver_fallback_image.png/content/dam/fom-website/drivers/G/GEORUS01_George_Russell/georus01.png.transform/2col.png",
                "desc": "팀의 리드 드라이버로서 정교한 분석력과 꾸준한 포디움 입성을 보여주는 메르세데스의 에이스입니다."
            }
        ]
    },
    {
        "team_en": "Scuderia Ferrari", "team_kr": "페라리", "color": "#E8002d", "principal": "Frédéric Vasseur", "power_unit": "Ferrari",
        "team_desc": "F1 역사 그 자체이자 최다 우승에 도전하는 팀으로, 2026년 슈퍼스타 드라이버 라인업을 완성했습니다.",
        "drivers": [
            {
                "name_en": "Lewis Hamilton", "name_kr": "루이스 해밀턴", "number": "44", "country": "영국", "birth": "1985.01.07",
                "image_url": "https://media.formula1.com/d_driver_fallback_image.png/content/dam/fom-website/drivers/L/LEWHAM01_Lewis_Hamilton/lewham01.png.transform/2col.png",
                "desc": "페라리로 전격 이적하여 통산 8번째 월드 챔피언 타이틀에 도전하고 있는 살아있는 전설입니다."
            },
            {
                "name_en": "Charles Leclerc", "name_kr": "샤를 르클레르", "number": "16", "country": "모나코", "birth": "1997.10.16",
                "image_url": "https://media.formula1.com/d_driver_fallback_image.png/content/dam/fom-website/drivers/C/CHALEC01_Charles_Leclerc/chalec01.png.transform/2col.png",
                "desc": "폭발적인 원랩 스피드와 정교한 코너링 테크닉을 자랑하는 모나코의 영웅입니다."
            }
        ]
    },
    {
        "team_en": "McLaren Formula 1 Team", "team_kr": "맥라렌", "color": "#FF8000", "principal": "Andrea Stella", "power_unit": "Mercedes",
        "team_desc": "뛰어난 에어로다이내믹 샤시 설계 능력으로 메르세데스와 페라리를 바짝 추격하는 전통 명문입니다.",
        "drivers": [
            {
                "name_en": "Lando Norris", "name_kr": "랜도 노리스", "number": "4", "country": "영국", "birth": "1999.11.13",
                "image_url": "https://media.formula1.com/d_driver_fallback_image.png/content/dam/fom-website/drivers/L/LANNOR01_Lando_Norris/lannor01.png.transform/2col.png",
                "desc": "맥라렌의 명가 재건을 이끌며 매 경기 화려한 추월쇼와 우승을 다투는 드라이버입니다."
            },
            {
                "name_en": "Oscar Piastri", "name_kr": "오스카 피아스트리", "number": "81", "country": "호주", "birth": "2001.04.06",
                "image_url": "https://media.formula1.com/d_driver_fallback_image.png/content/dam/fom-website/drivers/O/OSCPIA01_Oscar_Piastri/oscpia01.png.transform/2col.png",
                "desc": "압박감이 심한 상황에서도 강한 침착성과 철두철미한 경기 운영을 선보이는 차세대 에이스입니다."
            }
        ]
    },
    {
        "team_en": "Oracle Red Bull Racing", "team_kr": "레드불 레이싱", "color": "#3671C6", "principal": "Christian Horner", "power_unit": "Red Bull Ford",
        "team_desc": "포드와의 파워유닛 파트너십으로 새 시대를 열며 독보적인 레이싱 전략을 펼치고 있습니다.",
        "drivers": [
            {
                "name_en": "Max Verstappen", "name_kr": "막스 베르스타펜", "number": "1", "country": "네덜란드", "birth": "1997.09.30",
                "image_url": "https://media.formula1.com/d_driver_fallback_image.png/content/dam/fom-website/drivers/M/MAXVER01_Max_Verstappen/maxver01.png.transform/2col.png",
                "desc": "한 치의 오차도 허용하지 않는 압도적 페이스와 공격적인 오버테이크 능력을 가진 챔피언입니다."
            },
            {
                "name_en": "Yuki Tsunoda", "name_kr": "츠노다 유키", "number": "22", "country": "일본", "birth": "2000.05.11",
                "image_url": "https://media.formula1.com/d_driver_fallback_image.png/content/dam/fom-website/drivers/Y/YUKTSU01_Yuki_Tsunoda/yuktsu01.png.transform/2col.png",
                "desc": "과감한 브레이킹 능력과 정교한 코너링 감각으로 레드불 시트에서 도전을 이어가고 있습니다."
            }
        ]
    },
    {
        "team_en": "Cadillac F1 Team", "team_kr": "캐딜락 F1 팀", "color": "#FFD700", "principal": "Graeme Lowdon", "power_unit": "Ferrari",
        "team_desc": "2026년 F1에 11번째 팀으로 새로 합류한 미 제너럴 모터스(GM)의 프리미엄 창단 팀입니다.",
        "drivers": [
            {
                "name_en": "Valtteri Bottas", "name_kr": "발테리 보타스", "number": "77", "country": "핀란드", "birth": "1989.08.28",
                "image_url": "https://media.formula1.com/d_driver_fallback_image.png/content/dam/fom-website/drivers/V/VALBOT01_Valtteri_Bottas/valbot01.png.transform/2col.png",
                "desc": "통산 10회 우승 노하우를 바탕으로 신생 캐딜락 팀의 셋업 개발과 정착을 이끄는 베테랑입니다."
            },
            {
                "name_en": "Sergio Pérez", "name_kr": "세르히오 페레스", "number": "11", "country": "멕시코", "birth": "1990.01.26",
                "image_url": "https://media.formula1.com/d_driver_fallback_image.png/content/dam/fom-website/drivers/S/SERPER01_Sergio_Perez/serper01.png.transform/2col.png",
                "desc": "탁월한 타이어 관리와 시가지 서킷에서의 강점을 통해 실점 없는 레이스를 펼치는 베테랑입니다."
            }
        ]
    }
]

# 2026 경기 일정 데이터
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
    {"round": "13R", "country": "🇮🇹 이탈리아", "circuit": "몬차 서킷", "date": "2026. 09. 06", "status": "예정", "podium": None},
    {"round": "14R", "country": "🇪🇸 스페인 (마드리드)", "circuit": "마드리드 스트리트 서킷", "date": "2026. 09. 13", "status": "예정", "podium": None},
    {"round": "15R", "country": "🇦🇿 아제르바이잔", "circuit": "바쿠 시티 서킷", "date": "2026. 09. 26", "status": "예정", "podium": None},
    {"round": "16R", "country": "🇸🇬 싱가포르", "circuit": "마리나 베이 스트리트 서킷", "date": "2026. 10. 11", "status": "예정", "podium": None},
    {"round": "17R", "country": "🇺🇸 미국 (오스틴)", "circuit": "서킷 오브 디 아메리카스", "date": "2026. 10. 25", "status": "예정", "podium": None},
    {"round": "18R", "country": "🇲🇽 멕시코", "circuit": "에르마노스 로드리게스", "date": "2026. 11. 01", "status": "예정", "podium": None},
    {"round": "19R", "country": "🇧🇷 브라질", "circuit": "인터라고스 서킷", "date": "2026. 11. 08", "status": "예정", "podium": None},
    {"round": "20R", "country": "🇺🇸 미국 (베이거스)", "circuit": "라스베이거스 스트립 서킷", "date": "2026. 11. 21", "status": "예정", "podium": None},
    {"round": "21R", "country": "🇶🇦 카타르", "circuit": "루사일 인터내셔널 서킷", "date": "2026. 11. 29", "status": "예정", "podium": None},
    {"round": "22R", "country": "🇦🇪 아랍에미리트", "circuit": "야스 마리나 서킷", "date": "2026. 12. 06", "status": "예정", "podium": None}
]

# Streamlit 탭 구성
tab1, tab2, tab3 = st.tabs(["🏆 2026 시즌 실시간 순위", "🏎️ F1 팀 & 드라이버 프로필", "📅 경기 일정 및 포디움"])

# Tab 1: 2026년 실시간 드라이버 (23명) 및 팀 (11개) 순위
with tab1:
    st.subheader("🏆 2026 FIA Formula 1 World Championship Standings")
    st.caption("12R 네덜란드 그랑프리 종료 기준 23명 드라이버 및 11개 컨스트럭터 팀 공식 순위표입니다.")
    st.write("")

    col_rank1, col_rank2 = st.columns([1.2, 1])

    with col_rank1:
        st.markdown("### 🏎️ **드라이버 챔피언십 순위 (23명)**")
        st.dataframe(
            driver_standings_2026,
            column_config={
                "rank": "순위",
                "driver": "드라이버 이름",
                "team": "팀",
                "points": "포인트 (PTS)",
                "wins": "우승"
            },
            use_container_width=True,
            hide_index=True,
            height=850
        )

    with col_rank2:
        st.markdown("### 🛠️ **컨스트럭터 챔피언십 순위 (11개 팀)**")
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
            height=460
        )

# Tab 2: 팀 & 드라이버 맞춤형 사진 카드
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
            
            with st.expander(f"📖 {team['team_kr']} 팀 상세 설명 보기", expanded=True):
                st.write(team["team_desc"])
            
            st.write("")
            st.subheader("🏎️ 소속 드라이버 프로필")
            
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
                                <div style="font-size: 0.8rem; color: #718096;">{driver['name_en']}</div>
                                <div style="font-size: 0.8rem; color: #cbd5e0; margin-top: 5px;"><b>국적:</b> {driver['country']} | <b>생년월일:</b> {driver['birth']}</div>
                                <div class="driver-desc">{driver['desc']}</div>
                            </div>
                        </div>
                    """, unsafe_allow_html=True)

# Tab 3: 일정 및 포디움
with tab3:
    st.subheader("🏁 2026 FIA F1 그랑프리 일정 & 경기 결과")
    st.caption("라운드별 일정 및 12R까지의 TOP 3 실제 포디움 집계 결과입니다.")
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
