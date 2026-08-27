import streamlit as st

st.set_page_config(
    page_title="F1 2026 시즌 대시보드",
    page_icon="🏎️",
    layout="wide"
)

# Custom CSS - 상단 공백 제거, 로고 비율 유지 확대, 카드 디자인
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@600;800;900&family=Noto+Sans+KR:wght@400;700;900&display=swap');

    .stApp {
        background: linear-gradient(135deg, #07090f 0%, #11151f 50%, #030406 100%);
        color: #ffffff !important;
        font-family: 'Noto Sans KR', sans-serif;
    }

    /* Streamlit 상단 기본 여백 제거 */
    .block-container {
        padding-top: 0.5rem !important;
        padding-bottom: 2rem !important;
    }

    /* F1 로고 가로세로 비율 유지하며 큼직하게 확대 */
    .f1-logo-img {
        width: 100%;
        max-width: 280px;
        height: auto;
        object-fit: contain;
        filter: drop-shadow(0px 0px 12px rgba(225, 6, 0, 0.7));
    }

    .f1-accent-line {
        width: 100%;
        height: 2px;
        background: linear-gradient(90deg, transparent, #e10600, transparent);
        margin-bottom: 15px;
    }

    .stTabs {
        margin-top: -15px;
    }

    h1, h2, h3, h4, h5, h6, p, span, label, div {
        color: #ffffff !important;
    }

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

    .driver-big-num {
        font-family: 'Orbitron', sans-serif;
        font-size: 1.5rem;
        font-weight: 900;
        color: #ff3333 !important;
    }

    .driver-big-name {
        font-family: 'Noto Sans KR', sans-serif;
        font-size: 1.25rem;
        font-weight: 900;
        color: #ffffff !important;
        margin-top: 4px;
    }

    .driver-detail-box {
        background: #111622;
        border-radius: 12px;
        border: 2px solid #e10600;
        padding: 24px;
        margin-top: 20px;
        box-shadow: 0 6px 25px rgba(225, 6, 0, 0.3);
    }

    .space-util-box {
        background: rgba(18, 23, 33, 0.6);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 10px;
        padding: 15px;
        margin-top: 15px;
    }
    
    .race-card {
        background: rgba(18, 23, 33, 0.8);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 10px;
        padding: 18px;
        margin-bottom: 15px;
    }
    </style>
""", unsafe_allow_html=True)

# 2026 팀 및 확정 드라이버 번호 데이터
f1_teams_database = [
    {
        "team_en": "Mercedes-AMG Petronas F1 Team", "team_kr": "메르세데스", "color": "#27F4D2", "principal": "Toto Wolff", "power_unit": "Mercedes",
        "drivers": [
            {"name_en": "Kimi Antonelli", "name_kr": "키미 안토넬리", "number": "12", "country": "이탈리아 🇮🇹", "birth": "2006.08.25", "story": "주니어 시절부터 압도적인 기량을 증명하며 메르세데스 시트를 꿰찬 슈퍼 루키입니다."},
            {"name_en": "George Russell", "name_kr": "조지 러셀", "number": "63", "country": "영국 🇬🇧", "birth": "1998.02.15", "story": "치밀한 데이터 분석과 타협 없는 예선 주행 능력을 지닌 '미스터 토요일'입니다."}
        ]
    },
    {
        "team_en": "Scuderia Ferrari", "team_kr": "페라리", "color": "#E8002d", "principal": "Frédéric Vasseur", "power_unit": "Ferrari",
        "drivers": [
            {"name_en": "Lewis Hamilton", "name_kr": "루이스 해밀턴", "number": "44", "country": "영국 🇬🇧", "birth": "1985.01.07", "story": "통산 7회 월드 챔피언에 빛나는 F1 역사상 가장 성공한 드라이버입니다."},
            {"name_en": "Charles Leclerc", "name_kr": "샤를 르클레르", "number": "16", "country": "모나코 🇲🇨", "birth": "1997.10.16", "story": "페라리의 상징적인 원랩 스페셜리스트이자 폭발적인 스피드를 자랑하는 드라이버입니다."}
        ]
    },
    {
        "team_en": "McLaren Formula 1 Team", "team_kr": "맥라렌", "color": "#FF8000", "principal": "Andrea Stella", "power_unit": "Mercedes",
        "drivers": [
            {"name_en": "Lando Norris", "name_kr": "랜도 노리스", "number": "4", "country": "영국 🇬🇧", "birth": "1999.11.13", "story": "정교한 레이스 페이스 조율과 강인한 투지를 겸비한 맥라렌의 중심 에이스입니다."},
            {"name_en": "Oscar Piastri", "name_kr": "오스카 피아스트리", "number": "81", "country": "호주 🇦🇺", "birth": "2001.04.06", "story": "치열한 접전 속에서도 신입답지 않은 침착함과 노련함을 보여주는 천재 루키입니다."}
        ]
    },
    {
        "team_en": "Oracle Red Bull Racing", "team_kr": "레드불 레이싱", "color": "#3671C6", "principal": "Christian Horner", "power_unit": "Red Bull Ford",
        "drivers": [
            {"name_en": "Max Verstappen", "name_kr": "막스 베르스타펜", "number": "1", "country": "네덜란드 🇳🇱", "birth": "1997.09.30", "story": "정교한 레이스 장악력과 타협 없는 공격성으로 대변되는 최정상급 챔피언입니다."},
            {"name_en": "Isack Hadjar", "name_kr": "아이작 하자르", "number": "6", "country": "프랑스 🇫🇷", "birth": "2004.09.28", "story": "레드불 주니어 시스템을 거쳐 정식 시트에 오른 투지 넘치는 영건입니다."}
        ]
    },
    {
        "team_en": "Visa Cash App Racing Bulls", "team_kr": "레이싱 불스 (RB)", "color": "#6692FF", "principal": "Laurent Mekies", "power_unit": "Red Bull Ford",
        "drivers": [
            {"name_en": "Liam Lawson", "name_kr": "리암 로슨", "number": "30", "country": "뉴질랜드 🇳🇿", "birth": "2002.02.11", "story": "주어진 기회를 실력으로 입증해 내며 정식 시트를 거머쥔 뉴질랜드의 파이터입니다."},
            {"name_en": "Arvid Lindblad", "name_kr": "아르비드 린드블라드", "number": "41", "country": "영국 🇬🇧", "birth": "2007.08.08", "story": "차세대 유망주로 기대를 모으며 F1에 전격 합류한 초특급 루키입니다."}
        ]
    },
    {
        "team_en": "BWT Alpine F1 Team", "team_kr": "알핀", "color": "#FF87BC", "principal": "Oliver Oakes", "power_unit": "Mercedes",
        "drivers": [
            {"name_en": "Pierre Gasly", "name_kr": "피에르 개슬리", "number": "10", "country": "프랑스 🇫🇷", "birth": "1996.02.07", "story": "다양한 실전 경험을 바탕으로 팀을 이끄는 노련한 프랑스 국적의 드라이버입니다."},
            {"name_en": "Franco Colapinto", "name_kr": "프랑코 콜라핀토", "number": "43", "country": "아르헨티나 🇦🇷", "birth": "2003.05.27", "story": "남미 팬들의 열렬한 호응과 함께 F1 무대에 센세이션을 일으키며 합류했습니다."}
        ]
    },
    {
        "team_en": "TGR Haas F1 Team", "team_kr": "하스", "color": "#B6BABD", "principal": "Ayao Komatsu", "power_unit": "Ferrari",
        "drivers": [
            {"name_en": "Esteban Ocon", "name_kr": "에스테반 오콘", "number": "31", "country": "프랑스 🇫🇷", "birth": "1996.09.17", "story": "안정적인 방어 주행과 꾸준한 포인트 피니시 능력을 지닌 베테랑입니다."},
            {"name_en": "Oliver Bearman", "name_kr": "올리버 베어먼", "number": "87", "country": "영국 🇬🇧", "birth": "2005.05.08", "story": "비상한 주행 감각으로 전 세계 모터스포츠 팬들에게 깊은 인상을 남긴 실력파 유망주입니다."}
        ]
    },
    {
        "team_en": "Audi F1 Team", "team_kr": "아우디 (자우버)", "color": "#00E785", "principal": "Mattia Binotto", "power_unit": "Audi",
        "drivers": [
            {"name_en": "Nico Hülkenberg", "name_kr": "니코 휠켄베르크", "number": "27", "country": "독일 🇩🇪", "birth": "1987.08.19", "story": "F1에서 가장 정교하고 날카로운 예선 능력을 인정받는 독일의 베테랑입니다."},
            {"name_en": "Gabriel Bortoleto", "name_kr": "가브리에우 보르툴레투", "number": "5", "country": "브라질 🇧🇷", "birth": "2004.10.14", "story": "하위 포뮬러 무대를 평정하고 아우디의 미래를 책임질 메인 시트에 낙점되었습니다."}
        ]
    },
    {
        "team_en": "Atlassian Williams Racing", "team_kr": "윌리엄스", "color": "#64C4FF", "principal": "James Vowles", "power_unit": "Mercedes",
        "drivers": [
            {"name_en": "Carlos Sainz", "name_kr": "카를로스 사인츠", "number": "55", "country": "스페인 🇪🇸", "birth": "1994.09.01", "story": "철저한 전략 분석과 뛰어난 레이스 이해도를 갖춘 '전략가형' 드라이버입니다."},
            {"name_en": "Alexander Albon", "name_kr": "알렉산더 알본", "number": "23", "country": "태국 🇹🇭", "birth": "1996.03.23", "story": "까다로운 머신 세팅에서도 마법 같은 포인트 피니시를 만들어내는 실력파입니다."}
        ]
    },
    {
        "team_en": "Aston Martin Aramco F1 Team", "team_kr": "애스턴 마틴", "color": "#229971", "principal": "Andy Cowell", "power_unit": "Honda",
        "drivers": [
            {"name_en": "Fernando Alonso", "name_kr": "페르난도 알론소", "number": "14", "country": "스페인 🇪🇸", "birth": "1981.07.29", "story": "나이를 가늠할 수 없는 반사 신경과 독보적인 레이스 시야를 지닌 불멸의 전설입니다."},
            {"name_en": "Lance Stroll", "name_kr": "랜스 스트롤", "number": "18", "country": "캐나다 🇨🇦", "birth": "1998.10.29", "story": "변화무쌍한 기상 조건이나 혼전 상황에서 유독 빛을 발하는 드라이버입니다."}
        ]
    },
    {
        "team_en": "Cadillac F1 Team", "team_kr": "캐딜락 F1 팀", "color": "#FFD700", "principal": "Graeme Lowdon", "power_unit": "Ferrari",
        "drivers": [
            {"name_en": "Valtteri Bottas", "name_kr": "발테리 보타스", "number": "77", "country": "핀란드 🇫🇮", "birth": "1989.08.28", "story": "풍부한 우승 경력과 방대한 머신 개발 데이터를 지닌 베테랑 드라이버입니다."},
            {"name_en": "Sergio Pérez", "name_kr": "세르히오 페레스", "number": "11", "country": "멕시코 🇲🇽", "birth": "1990.01.26", "story": "시가지 서킷에서 특히 강한 면모를 보이며 타이어 관리 능력이 뛰어납니다."}
        ]
    }
]

# 2026 그랑프리 일정 데이터
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

if "selected_driver" not in st.session_state:
    st.session_state.selected_driver = None

if "previous_team" not in st.session_state:
    st.session_state.previous_team = None

# 상단 로고 및 탭 배치
col_logo, col_tabs = st.columns([1.3, 3.7])

with col_logo:
    st.markdown("""
        <div style="display: flex; align-items: center; height: 100%; padding-top: 5px;">
            <img class="f1-logo-img" src="https://upload.wikimedia.org/wikipedia/commons/3/33/F1.svg" alt="F1 Logo">
        </div>
    """, unsafe_allow_html=True)

with col_tabs:
    tab1, tab2 = st.tabs([
        "🔍 F1 팀 & 선수 정보", 
        "ℹ️ 시즌 소개"
    ])

st.markdown('<div class="f1-accent-line"></div>', unsafe_allow_html=True)

# [탭 1] 팀 & 선수 정보 화면
with tab1:
    st.write("")
    main_col, side_col = st.columns([2.2, 1.8])
    
    with main_col:
        team_name_list = [t["team_kr"] for t in f1_teams_database]
        selected_search_team = st.selectbox("검색할 팀 선택", team_name_list)
        
        # 팀을 변경했을 때 이전 드라이버 선택 기록 초기화
        if st.session_state.previous_team != selected_search_team:
            st.session_state.selected_driver = None
            st.session_state.previous_team = selected_search_team
        
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
                
                st.markdown("### 👥 소속 드라이버 선택")
                d_cols = st.columns(2)
                
                for idx, driver in enumerate(team["drivers"]):
                    with d_cols[idx]:
                        btn_label = f"#{driver['number']}   |   {driver['name_kr']}"
                        if st.button(btn_label, key=f"btn_{driver['number']}_{driver['name_en']}", use_container_width=True):
                            st.session_state.selected_driver = driver

        if st.session_state.selected_driver:
            d = st.session_state.selected_driver
            st.markdown(f"""
                <div class="driver-detail-box">
                    <div style="display: flex; align-items: baseline; gap: 15px; margin-bottom: 10px;">
                        <span class="driver-big-num">#{d['number']}</span>
                        <span class="driver-big-name">{d['name_kr']} ({d['name_en']})</span>
                    </div>
                    <p style="margin: 4px 0; font-size: 1rem; color: #cbd5e1;"><b>국적:</b> {d['country']} &nbsp;|&nbsp; <b>생년월일:</b> {d['birth']}</p>
                    <hr style="border-color: rgba(255,255,255,0.15); margin: 12px 0;">
                    <p style="font-size: 1.05rem; line-height: 1.7; color: #f1f5f9; margin-bottom: 0;">
                        {d['story']}
                    </p>
                </div>
            """, unsafe_allow_html=True)

    with side_col:
        st.markdown("""
            <div class="space-util-box">
                <h4 style="color: #ff3333; margin-top: 0; font-family: 'Orbitron', sans-serif;">⚡ 2026 시즌 하이라이트</h4>
                <p style="font-size: 0.95rem; line-height: 1.6; color: #cbd5e1;">
                • <b>2026 규정 대변혁:</b> 완전히 새롭게 바뀐 액티브 파워유닛과 경량화된 공기역학 머신 도입.<br><br>
                • <b>신생 팀 합류:</b> 캐딜락 F1 팀이 새롭게 그리드에 합류하여 총 11개 팀 체제로 확장.<br><br>
                • <b>치열한 세대교체:</b> 메르세데스의 앤토넬리를 비롯한 영건들과 베테랑들의 타이틀 매치!
                </p>
            </div>
        """, unsafe_allow_html=True)
        
        completed_races = sum(1 for r in f1_races_2026 if r["status"] == "완료")
        total_races = len(f1_races_2026)
        progress_val = completed_races / total_races
        
        st.markdown(f"""
            <div class="space-util-box" style="margin-top: 15px;">
                <h4 style="color: #27F4D2; margin-top: 0; font-family: 'Orbitron', sans-serif;">📊 2026 캘린더 진행률</h4>
                <p style="font-size: 0.95rem; color: #e2e8f0; margin-bottom: 8px;">총 {total_races}라운드 중 <b>{completed_races}라운드</b> 완료</p>
            </div>
        """, unsafe_allow_html=True)
        st.progress(progress_val)

# [탭 2] 간단한 시즌 소개
with tab2:
    st.write("")
    st.markdown("### 🏎️ 2026 FIA 포뮬러 원 월드 챔피언십")
    st.write("2026년은 새로운 엔진 규정과 11개의 컨스트럭터가 격돌하는 대변혁의 시즌입니다.")

# ==========================================
# ⬇️ 메인 화면 아래쪽 빈 공간: 전체 일정표 & 포디움 결과
# ==========================================
st.markdown("<br>", unsafe_allow_html=True)
st.markdown('<div class="f1-accent-line"></div>', unsafe_allow_html=True)
st.markdown("## 📅 2026 시즌 전체 그랑프리 일정표 및 포디움 결과")
st.write("지금까지 완료된 경기의 포디움(TOP 3) 기록과 다가오는 전체 레이스 일정을 확인하세요.")
st.write("")

schedule_col, podium_col = st.columns(2)

with schedule_col:
    st.markdown("### 🗓️ 전체 레이스 캘린더")
    for race in f1_races_2026:
        status_color = "#27F4D2" if race['status'] == '완료' else "#ff9900"
        status_text = "✅ 완료" if race['status'] == '완료' else "⏳ 예정"
        
        st.markdown(f"""
            <div class="race-card" style="padding: 12px 15px; margin-bottom: 10px;">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <span style="font-family: 'Orbitron', sans-serif; font-size: 1rem; font-weight: bold; color: #ff3333;">{race['round']}</span>
                    <span style="background: rgba(255,255,255,0.1); padding: 2px 8px; border-radius: 10px; font-size: 0.8rem; color: {status_color}; font-weight: bold;">{status_text}</span>
                </div>
                <h4 style="margin: 4px 0 2px 0; font-size: 1.05rem;">{race['country']}</h4>
                <p style="margin: 0; color: #94a3b8; font-size: 0.85rem;">📍 {race['circuit']} | 📅 {race['date']}</p>
            </div>
        """, unsafe_allow_html=True)

with podium_col:
    st.markdown("### 🏆 완료된 경기 포디움 (TOP 3)")
    completed_list = [r for r in f1_races_2026 if r["status"] == "완료"]
    
    for race in completed_list:
        podium_str = "<br>".join([f"• {p}" for p in race["podium"]])
        st.markdown(f"""
            <div class="race-card" style="border-left: 4px solid #e10600; padding: 12px 15px; margin-bottom: 10px;">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <span style="font-family: 'Orbitron', sans-serif; font-size: 0.95rem; font-weight: bold; color: #ff3333;">{race['round']} - {race['country']}</span>
                    <span style="color: #94a3b8; font-size: 0.8rem;">{race['date']}</span>
                </div>
                <div style="background: rgba(0,0,0,0.3); padding: 8px 12px; border-radius: 6px; font-size: 0.9rem; line-height: 1.5; margin-top: 6px;">
                    {podium_str}
                </div>
            </div>
        """, unsafe_allow_html=True)
