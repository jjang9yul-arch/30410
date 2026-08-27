import streamlit as st

# 1. 페이지 와이드 설정
st.set_page_config(
    page_title="F1 2026 통합 포털",
    page_icon="🏎️",
    layout="wide"
)

# 2. CSS 스타일링 (하얀 글씨, 전체 칸 활용, 컴팩트한 F1 로고 및 깔끔한 카테고리 카드)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@600;800;900&family=Noto+Sans+KR:wght@400;700;900&display=swap');

    .stApp {
        background: linear-gradient(135deg, #0b0e14 0%, #151a24 50%, #05070a 100%);
        color: #ffffff !important;
        font-family: 'Noto Sans KR', sans-serif;
    }

    /* 상단 헤더 컨테이너: F1 로고 크기를 적당히 줄이고 여백 최소화 */
    .f1-header-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        padding: 5px 0 10px 0;
        margin-bottom: 15px;
    }

    .f1-logo-img {
        width: 100%;
        max-width: 320px; 
        height: auto;
        object-fit: contain;
        filter: drop-shadow(0px 0px 15px rgba(225, 6, 0, 0.7));
        margin-bottom: 6px;
    }

    .f1-accent-line {
        width: 100%;
        max-width: 100%;
        height: 2px;
        background: linear-gradient(90deg, transparent, #e10600, transparent);
    }

    /* 모든 텍스트 하얀색 보장 */
    h1, h2, h3, h4, h5, h6, p, span, label, div {
        color: #ffffff !important;
    }

    /* 팀 카드 및 검색 카드 디자인 */
    .team-card {
        background: rgba(22, 27, 38, 0.95);
        border-radius: 12px;
        border: 1px solid rgba(255, 255, 255, 0.15);
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
        color: #ff6b6b !important;
        padding: 4px 12px;
        border-radius: 15px;
        font-size: 0.85rem;
        font-weight: 600;
        margin-right: 8px;
        margin-top: 8px;
    }

    /* 드라이버 프로필 카드 */
    .profile-card {
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
        font-weight: 700;
        color: #ffffff !important;
        margin: 4px 0;
    }
    </style>
""", unsafe_allow_html=True)

# 3. 상단 헤더 (크기 줄인 F1 로고 + 얇은 악센트 라인)
st.markdown("""
    <div class="f1-header-container">
        <img class="f1-logo-img" src="https://upload.wikimedia.org/wikipedia/commons/3/33/F1.svg" alt="F1 Logo">
        <div class="f1-accent-line"></div>
    </div>
""", unsafe_allow_html=True)

# 2026년 11개 팀 전체 데이터베이스 (각 팀별 드라이버 2명씩 총 22명 완벽 수록)
f1_teams_database = [
    {
        "team_en": "Mercedes-AMG Petronas F1 Team", "team_kr": "메르세데스", "color": "#27F4D2", "principal": "Toto Wolff", "power_unit": "Mercedes",
        "team_desc": "2026년 파워유닛 규정 변경에 완벽히 적응하여 챔피언십 선두를 질주하는 최강의 피트 팀입니다.",
        "drivers": [
            {"name_en": "Kimi Antonelli", "name_kr": "키미 안토넬리", "number": "12", "country": "이탈리아 🇮🇹", "birth": "2006.08.25", "desc": "6승을 올리며 드라이버 챔피언십 선두를 달리는 슈퍼 루키."},
            {"name_en": "George Russell", "name_kr": "조지 러셀", "number": "63", "country": "영국 🇬🇧", "birth": "1998.02.15", "desc": "정교한 분석력과 꾸준한 포디움 입성을 보여주는 메르세데스의 에이스."}
        ]
    },
    {
        "team_en": "Scuderia Ferrari", "team_kr": "페라리", "color": "#E8002d", "principal": "Frédéric Vasseur", "power_unit": "Ferrari",
        "team_desc": "F1 역사 최다 우승에 도전하는 이탈리아의 전설적인 프랜차이즈 팀입니다.",
        "drivers": [
            {"name_en": "Lewis Hamilton", "name_kr": "루이스 해밀턴", "number": "44", "country": "영국 🇬🇧", "birth": "1985.01.07", "desc": "페라리로 이적해 통산 8번째 월드 챔피언 타이틀에 도전하는 전설."},
            {"name_en": "Charles Leclerc", "name_kr": "샤를 르클레르", "number": "16", "country": "모나코 🇲🇨", "birth": "1997.10.16", "desc": "폭발적인 원랩 스피드와 정교한 코너링 테크닉을 자랑하는 모나코의 영웅."}
        ]
    },
    {
        "team_en": "McLaren Formula 1 Team", "team_kr": "맥라렌", "color": "#FF8000", "principal": "Andrea Stella", "power_unit": "Mercedes",
        "team_desc": "뛰어난 에어로다이내믹 샤시 설계 능력으로 상위권을 지배하는 전통의 명문 팀입니다.",
        "drivers": [
            {"name_en": "Lando Norris", "name_kr": "랜도 노리스", "number": "4", "country": "영국 🇬🇧", "birth": "1999.11.13", "desc": "맥라렌의 명가 재건을 이끌며 매 경기 우승을 다투는 에이스."},
            {"name_en": "Oscar Piastri", "name_kr": "오스카 피아스트리", "number": "81", "country": "호주 🇦🇺", "birth": "2001.04.06", "desc": "압박 속에서도 강한 침착성과 철두철미한 경기 운영을 선보이는 드라이버."}
        ]
    },
    {
        "team_en": "Oracle Red Bull Racing", "team_kr": "레드불 레이싱", "color": "#3671C6", "principal": "Christian Horner", "power_unit": "Red Bull Ford",
        "team_desc": "포드와의 파워유닛 파트너십을 통해 새로운 시대를 열어가는 강호 팀입니다.",
        "drivers": [
            {"name_en": "Max Verstappen", "name_kr": "막스 베르스타펜", "number": "1", "country": "네덜란드 🇳🇱", "birth": "1997.09.30", "desc": "한 치의 오차도 없는 압도적 페이스와 공격적인 오버테이크의 챔피언."},
            {"name_en": "Isack Hadjar", "name_kr": "아이작 하자르", "number": "6", "country": "프랑스 🇫🇷", "birth": "2004.09.28", "desc": "레드불 주니어에서 승격되어 새로운 기회를 맞이한 신예 드라이버."}
        ]
    },
    {
        "team_en": "Visa Cash App Racing Bulls", "team_kr": "레이싱 불스 (RB)", "color": "#6692FF", "principal": "Laurent Mekies", "power_unit": "Red Bull Ford",
        "team_desc": "젊고 유능한 인재들을 발굴하며 레드불 그룹의 핵심 전력으로 활약하는 팀입니다.",
        "drivers": [
            {"name_en": "Liam Lawson", "name_kr": "리암 로슨", "number": "30", "country": "뉴질랜드 🇳🇿", "birth": "2002.02.11", "desc": "투지 넘치는 레이싱 스타일로 팀의 포인트 획득을 이끄는 드라이버."},
            {"name_en": "Arvid Lindblad", "name_kr": "아르비드 린드블라드", "number": "41", "country": "영국 🇬🇧", "birth": "2007.08.08", "desc": "F2를 거쳐 F1 무대에 전격 데뷔한 초특급 루키."}
        ]
    },
    {
        "team_en": "BWT Alpine F1 Team", "team_kr": "알핀", "color": "#FF87BC", "principal": "Oliver Oakes", "power_unit": "Mercedes",
        "team_desc": "프랑스의 기술력과 열정을 바탕으로 중위권 반등을 노리는 워크스 팀입니다.",
        "drivers": [
            {"name_en": "Pierre Gasly", "name_kr": "피에르 개슬리", "number": "10", "country": "프랑스 🇫🇷", "birth": "1996.02.07", "desc": "차량 한계 이상의 퍼포먼스를 이끌어내는 베테랑 드라이버."},
            {"name_en": "Franco Colapinto", "name_kr": "프랑코 콜라핀토", "number": "43", "country": "아르헨티나 🇦🇷", "birth": "2003.05.27", "desc": "안정적인 경기 운영과 빠른 적응력을 보여주는 아르헨티나의 스타."}
        ]
    },
    {
        "team_en": "TGR Haas F1 Team", "team_kr": "하스", "color": "#B6BABD", "principal": "Ayao Komatsu", "power_unit": "Ferrari",
        "team_desc": "미국 본토의 색깔을 담아 효율적이고 단단한 중위권 레이스를 펼치는 팀입니다.",
        "drivers": [
            {"name_en": "Esteban Ocon", "name_kr": "에스테반 오콘", "number": "31", "country": "프랑스 🇫🇷", "birth": "1996.09.17", "desc": "타이어 매니지먼트와 노련한 레이스 크래프트가 돋보이는 드라이버."},
            {"name_en": "Oliver Bearman", "name_kr": "올리버 베어먼", "number": "87", "country": "영국 🇬🇧", "birth": "2005.05.08", "desc": "페라리 아카데미 출신으로 풀타임 시트를 꿰찬 차세대 기대주."}
        ]
    },
    {
        "team_en": "Audi F1 Team", "team_kr": "아우디 (자우버)", "color": "#00E785", "principal": "Mattia Binotto", "power_unit": "Audi",
        "team_desc": "2026년 아우디 브랜드로 완전히 새롭게 태어난 대규모 워크스 프로젝트 팀입니다.",
        "drivers": [
            {"name_en": "Nico Hülkenberg", "name_kr": "니코 휠켄베르크", "number": "27", "country": "독일 🇩🇪", "birth": "1987.08.19", "desc": "독보적인 예선 스피드와 풍부한 경험으로 팀의 개발을 이끄는 베테랑."},
            {"name_en": "Gabriel Bortoleto", "name_kr": "가브리에우 보르툴레투", "number": "5", "country": "브라질 🇧🇷", "birth": "2004.10.14", "desc": "하위 포뮬러 챔피언 출신으로 아우디의 미래를 책임질 루키."}
        ]
    },
    {
        "team_en": "Atlassian Williams Racing", "team_kr": "윌리엄스", "color": "#64C4FF", "principal": "James Vowles", "power_unit": "Mercedes",
        "team_desc": "유서 깊은 영국의 명문 팀으로, 부활을 향한 기술적 도약을 이뤄내고 있습니다.",
        "drivers": [
            {"name_en": "Carlos Sainz", "name_kr": "카를로스 사인츠", "number": "55", "country": "스페인 🇪🇸", "birth": "1994.09.01", "desc": "탁월한 엔지니어링 피드백과 지능적인 레이스 운영 능력을 가진 베테랑."},
            {"name_en": "Alexander Albon", "name_kr": "알렉산더 알본", "number": "23", "country": "태국 🇹🇭", "birth": "1996.03.23", "desc": "어려운 차량 환경에서도 팀에 소중한 포인트를 안겨주는 윌리엄스의 리더."}
        ]
    },
    {
        "team_en": "Aston Martin Aramco F1 Team", "team_kr": "애스턴 마틴", "color": "#229971", "principal": "Andy Cowell", "power_unit": "Honda",
        "team_desc": "혼다 파워유닛과의 협력을 통해 최상위권 도약을 준비하는 브리티시 럭셔리 팀입니다.",
        "drivers": [
            {"name_en": "Fernando Alonso", "name_kr": "페르난도 알론소", "number": "14", "country": "스페인 🇪🇸", "birth": "1981.07.29", "desc": "살아있는 전설이자 경이로운 경기 감각을 유지하고 있는 불꽃 베테랑."},
            {"name_en": "Lance Stroll", "name_kr": "랜스 스트롤", "number": "18", "country": "캐나다 🇨🇦", "birth": "1998.10.29", "desc": "비 오는 서킷이나 혼전 속에서 뛰어난 집중력을 발휘하는 드라이버."}
        ]
    },
    {
        "team_en": "Cadillac F1 Team", "team_kr": "캐딜락 F1 팀", "color": "#FFD700", "principal": "Graeme Lowdon", "power_unit": "Ferrari",
        "team_desc": "2026년 F1에 11번째 팀으로 새롭게 합류한 미국의 제너럴 모터스(GM) 창단 팀입니다.",
        "drivers": [
            {"name_en": "Valtteri Bottas", "name_kr": "발테리 보타스", "number": "77", "country": "핀란드 🇫🇮", "birth": "1989.08.28", "desc": "통산 10승의 노하우를 바탕으로 신생 팀의 기준점을 제시하는 베테랑."},
            {"name_en": "Sergio Pérez", "name_kr": "세르히오 페레스", "number": "11", "country": "멕시코 🇲🇽", "birth": "1990.01.26", "desc": "노련한 경기 운영과 뛰어난 추월 능력을 보유한 베테랑 드라이버."}
        ]
    }
]

# 2026 그랑프리 일정 및 포디움 결과 데이터 (12R 완료, 13R 이후 예정)
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

# 4. 카테고리(탭) 생성
tab1, tab2, tab3 = st.tabs(["🔍 F1 팀 검색 & 드라이버", "🏎️ 2026 전체 11개 팀 백과사전", "📅 2026 그랑프리 일정 & 포디움"])

# [탭 1] 팀 검색 및 드라이버 상세 조회 기능
with tab1:
    st.subheader("🔍 F1 팀 검색 시스템")
    st.caption("원하시는 팀 이름(예: 페라리, 메르세데스, 레드불, 캐딜락 등)을 검색하거나 선택하세요.")
    
    team_name_list = [t["team_kr"] for t in f1_teams_database]
    selected_search_team = st.selectbox("팀 선택하기", team_name_list)
    
    for team in f1_teams_database:
        if team["team_kr"] == selected_search_team:
            st.markdown(f"""
                <div class="team-card" style="border-top: 5px solid {team['color']};">
                    <div class="team-title" style="color: {team['color']};">{team['team_en']} ({team['team_kr']})</div>
                    <p style="margin: 10px 0 15px 0; font-size: 1.05rem; color: #ffffff;">{team['team_desc']}</p>
                    <div>
                        <span class="stat-badge">팀 감독: {team['principal']}</span>
                        <span class="stat-badge">파워 유닛: {team['power_unit']}</span>
                    </div>
                </div>
            """, unsafe_allow_html=True)
            
            st.markdown("### 👥 소속 드라이버 정보 (국적 및 생년월일)")
            d_cols = st.columns(2)
            for idx, driver in enumerate(team["drivers"]):
                with d_cols[idx]:
                    st.markdown(f"""
                        <div class="profile-card">
                            <div class="driver-num">#{driver['number']}</div>
                            <div class="driver-name">{driver['name_kr']} ({driver['name_en']})</div>
                            <hr style="border-color: rgba(255,255,255,0.1); margin: 8px 0;">
                            <p style="margin: 4px 0; color: #e2e8f0;"><b>국적:</b> {driver['country']}</p>
                            <p style="margin: 4px 0; color: #e2e8f0;"><b>생년월일:</b> {driver['birth']}</p>
                            <p style="margin-top: 8px; color: #cbd5e0; font-size: 0.9rem;">{driver['desc']}</p>
                        </div>
                    """, unsafe_allow_html=True)

# [탭 2] 2026 전체 11개 팀 및 소속 드라이버 전체 노출
with tab2:
    st.subheader("🏁 2026 시즌 공식 11개 팀 & 드라이버 전체 라인업")
    st.caption("신생 캐딜락 F1 팀을 포함한 모든 컨스트럭터의 상세 정보와 드라이버 프로필입니다.")
    st.write("")

    for team in f1_teams_database:
        st.markdown(f"""
            <div class="team-card" style="border-left: 6px solid {team['color']};">
                <div class="team-title" style="color: {team['color']};">{team['team_en']} ({team['team_kr']})</div>
                <p style="margin: 8px 0; color: #ffffff;">{team['team_desc']}</p>
                <div>
                    <span class="stat-badge">감독: {team['principal']}</span>
                    <span class="stat-badge">엔진: {team['power_unit']}</span>
                </div>
            </div>
        """, unsafe_allow_html=True)
        
        c_cols = st.columns(2)
        for i, driver in enumerate(team["drivers"]):
            with c_cols[i]:
                st.markdown(f"""
                    <div class="profile-card">
                        <div class="driver-num">#{driver['number']}</div>
                        <div class="driver-name">{driver['name_kr']} ({driver['name_en']})</div>
                        <p style="margin: 3px 0; font-size: 0.9rem; color: #e2e8f0;">국적: {driver['country']} | 생년월일: {driver['birth']}</p>
                        <p style="margin-top: 6px; font-size: 0.85rem; color: #cbd5e0;">{driver['desc']}</p>
                    </div>
                """, unsafe_allow_html=True)
        st.write("---")

# [탭 3] 2026 그랑프리 일정표 및 포디움 순위 비교
with tab3:
    st.subheader("📅 2026 FIA F1 월드 챔피언십 전체 일정 & 포디움 결과")
    st.caption("이미 완료된 그랑프리는 우측에 실제 2026 포디움(TOP 3) 결과가 함께 표시됩니다.")
    st.write("")

    for race in f1_races_2026:
        with st.container():
            col_info, col_podium = st.columns([1.2, 1.8])
            
            with col_info:
                st.markdown(f"### **{race['round']} - {race['country']}**")
                st.write(f"📍 **서킷:** {race['circuit']}")
                st.write(f"📅 **일정:** {race['date']}")
                st.write(f"📌 **상태:** {'✅ 완료됨' if race['status'] == '완료' else '⏳ 경기 예정'}")
            
            with col_podium:
                if race["status"] == "완료" and len(race["podium"]) > 0:
                    st.markdown("##### 🏆 **포디움 (TOP 3 결과)**")
                    for p in race["podium"]:
                        st.markdown(f"- {p}")
                else:
                    st.info("아직 진행되지 않은 다가오는 그랑프리 경기입니다.")
            
            st.markdown("---")
