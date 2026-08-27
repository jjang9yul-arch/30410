import streamlit as st

st.set_page_config(
    page_title="F1 2026 시즌 대시보드",
    page_icon="🏎️",
    layout="wide"
)

# Custom CSS - 상단 공백을 완전히 박멸하고 F1 로고 및 빨간 줄을 완전히 제거
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@600;800;900&family=Noto+Sans+KR:wght@400;700;900&display=swap');

    .stApp {
        background: linear-gradient(135deg, #07090f 0%, #11151f 50%, #030406 100%);
        color: #ffffff !important;
        font-family: 'Noto Sans KR', sans-serif;
    }

    /* Streamlit 상단 기본 여백 완전 박멸 */
    header[data-testid="stHeader"] {
        background: transparent;
        display: none;
    }

    .block-container {
        padding-top: 0rem !important;
        padding-bottom: 2rem !important;
        margin-top: -3rem !important;
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

    /* 드라이버 심층 설명 박스 */
    .driver-detail-box {
        background: #111622;
        border-radius: 12px;
        border: 1px solid #e10600;
        padding: 22px;
        margin-top: 15px;
        box-shadow: 0 4px 20px rgba(225, 6, 0, 0.25);
    }
    </style>
""", unsafe_allow_html=True)

# 2026 시즌 전체 11개 팀 및 22명 선수 데이터베이스 (서사 포함)
f1_teams_database = [
    {
        "team_en": "Mercedes-AMG Petronas F1 Team", "team_kr": "메르세데스", "color": "#27F4D2", "principal": "Toto Wolff", "power_unit": "Mercedes",
        "drivers": [
            {"name_en": "Kimi Antonelli", "name_kr": "키미 안토넬리", "number": "12", "country": "이탈리아 🇮🇹", "birth": "2006.08.25", "story": "주니어 시절부터 압도적인 재능으로 '넥스트 베르스타펜'으로 지목받았습니다. 메르세데스 메인 시트에 데뷔하자마자 시즌 초반부터 경이로운 주행을 선보이며 수차례 우승을 거머쥔 2026시즌 최강의 영건입니다."},
            {"name_en": "George Russell", "name_kr": "조지 러셀", "number": "63", "country": "영국 🇬🇧", "birth": "1998.02.15", "story": "극단적인 예선 집중력과 타협 없는 주행을 보여주는 '미스터 토요일'입니다. 냉철한 판단력으로 은빛 화살 메르세데스의 황금기를 이끌고 있는 팀의 든든한 리더입니다."}
        ]
    },
    {
        "team_en": "Scuderia Ferrari", "team_kr": "페라리", "color": "#E8002d", "principal": "Frédéric Vasseur", "power_unit": "Ferrari",
        "drivers": [
            {"name_en": "Lewis Hamilton", "name_kr": "루이스 해밀턴", "number": "44", "country": "영국 🇬🇧", "birth": "1985.01.07", "story": "통산 7회 월드 챔피언에 빛나는 F1 역사상 가장 위대한 살아있는 전설입니다. 페라리로 이적하여 스칼렛 레드 머신을 타고 통산 8번째 월드 타이틀을 향해 목숨을 건 레이스를 펼치고 있습니다."},
            {"name_en": "Charles Leclerc", "name_kr": "샤를 르클레르", "number": "16", "country": "모나코 🇲🇨", "birth": "1997.10.16", "story": "페라리가 배출한 역대급 원랩 스페셜리스트이자 모나코의 영웅입니다. 한계 상황에서 코너링의 극한을 이끌어내는 공격적인 드라이빙이 무기입니다."}
        ]
    },
    {
        "team_en": "McLaren Formula 1 Team", "team_kr": "맥라렌", "color": "#FF8000", "principal": "Andrea Stella", "power_unit": "Mercedes",
        "drivers": [
            {"name_en": "Lando Norris", "name_kr": "랜도 노리스", "number": "4", "country": "영국 🇬🇧", "birth": "1999.11.13", "story": "재치 있는 성격 뒤에 폭발적인 투지와 천재적인 감각을 숨긴 맥라렌의 메인 에이스입니다. 꾸준한 성장세로 매 시즌 우승 트로피를 사냥하고 있습니다."},
            {"name_en": "Oscar Piastri", "name_kr": "오스카 피아스트리", "number": "81", "country": "호주 🇦🇺", "birth": "2001.04.06", "story": "주니어 시리즈를 휩쓸고 F1에 입성한 '포커페이스의 천재'입니다. 치열한 접전 중에도 신입답지 않은 서늘한 침착성과 완벽한 타이어 매니지먼트를 자랑합니다."}
        ]
    },
    {
        "team_en": "Oracle Red Bull Racing", "team_kr": "레드불 레이싱", "color": "#3671C6", "principal": "Christian Horner", "power_unit": "Red Bull Ford",
        "drivers": [
            {"name_en": "Max Verstappen", "name_kr": "막스 베르스타펜", "number": "1", "country": "네덜란드 🇳🇱", "birth": "1997.09.30", "story": "타협 없는 공격성과 정교한 주행 능력으로 F1 패러다임을 바꾼 괴물 같은 챔피언입니다. 차량 성능의 열세 속에서도 기적 같은 포인트를 짜내고 있습니다."},
            {"name_en": "Isack Hadjar", "name_kr": "아이작 하자르", "number": "6", "country": "프랑스 🇫🇷", "birth": "2004.09.28", "story": "레드불 주니어 프로그램의 거친 검증을 통과해 정식 시트를 꿰찬 투지 넘치는 신예입니다. 거침없는 패기로 세계 최고의 드라이버들과 어깨를 나란히 합니다."}
        ]
    },
    {
        "team_en": "Visa Cash App Racing Bulls", "team_kr": "레이싱 불스 (RB)", "color": "#6692FF", "principal": "Laurent Mekies", "power_unit": "Red Bull Ford",
        "drivers": [
            {"name_en": "Liam Lawson", "name_kr": "리암 로슨", "number": "30", "country": "뉴질랜드 🇳🇿", "birth": "2002.02.11", "story": "대타 출전 기회를 실력으로 증명해 내며 정식 시트를 거머쥔 뉴질랜드의 파이터입니다. 몸을 사리지 않는 과감한 추월 능력을 지니고 있습니다."},
            {"name_en": "Arvid Lindblad", "name_kr": "아르비드 린드블라드", "number": "41", "country": "영국 🇬🇧", "birth": "2007.08.08", "story": "초고속으로 F1 무대에 승선한 특급 루키입니다. 나이가 믿기지 않는 대담한 레이스 운영과 영리한 경기 조율 능력을 보여줍니다."}
        ]
    },
    {
        "team_en": "BWT Alpine F1 Team", "team_kr": "알핀", "color": "#FF87BC", "principal": "Oliver Oakes", "power_unit": "Mercedes",
        "drivers": [
            {"name_en": "Pierre Gasly", "name_kr": "피에르 개슬리", "number": "10", "country": "프랑스 🇫🇷", "birth": "1996.02.07", "story": "수많은 시련을 딛고 일어선 불굴의 레이서이자 감격스러운 우승 경험을 지닌 베테랑입니다. 알핀의 든든한 정신적 지주 역할을 맡고 있습니다."},
            {"name_en": "Franco Colapinto", "name_kr": "프랑코 콜라핀토", "number": "43", "country": "아르헨티나 🇦🇷", "birth": "2003.05.27", "story": "남미 팬들의 열광적인 지지를 업고 F1 무대에 센세이션을 일으키며 합류했습니다. 뛰어난 피드백 능력으로 팀에 활력을 불어넣고 있습니다."}
        ]
    },
    {
        "team_en": "TGR Haas F1 Team", "team_kr": "하스", "color": "#B6BABD", "principal": "Ayao Komatsu", "power_unit": "Ferrari",
        "drivers": [
            {"name_en": "Esteban Ocon", "name_kr": "에스테반 오콘", "number": "31", "country": "프랑스 🇫🇷", "birth": "1996.09.17", "story": "철저한 타이어 관리와 정교한 방어 주행이 특기인 베테랑 프랑스 드라이버입니다. 까다로운 트랙 상황에서도 집중력을 잃지 않고 점수를 긁어모읍니다."},
            {"name_en": "Oliver Bearman", "name_kr": "올리버 베어먼", "number": "87", "country": "영국 🇬🇧", "birth": "2005.05.08", "story": "페라리 대타 출전 당시 천재적인 주행으로 전 세계를 경악게 했던 주역입니다. 젊은 나이에도 침착한 경기 흐름 파악 능력을 겸비했습니다."}
        ]
    },
    {
        "team_en": "Audi F1 Team", "team_kr": "아우디 (자우버)", "color": "#00E785", "principal": "Mattia Binotto", "power_unit": "Audi",
        "drivers": [
            {"name_en": "Nico Hülkenberg", "name_kr": "니코 휠켄베르크", "number": "27", "country": "독일 🇩🇪", "birth": "1987.08.19", "story": "F1에서 가장 정교하고 날카로운 예선 한 방 능력을 지닌 독일 모터스포츠의 상징입니다. 아우디 프로젝트의 첫 초석을 다지는 중책을 맡고 있습니다."},
            {"name_en": "Gabriel Bortoleto", "name_kr": "가브리에우 보르툴레투", "number": "5", "country": "브라질 🇧🇷", "birth": "2004.10.14", "story": "하위 포뮬러를 제패한 뒤 아우디의 미래를 책임질 메인 시트에 낙점된 브라질의 신예입니다. 영리하고 안정적인 포인트 피니시가 강점입니다."}
        ]
    },
    {
        "team_en": "Atlassian Williams Racing", "team_kr": "윌리엄스", "color": "#64C4FF", "principal": "James Vowles", "power_unit": "Mercedes",
        "drivers": [
            {"name_en": "Carlos Sainz", "name_kr": "카를로스 사인츠", "number": "55", "country": "스페인 🇪🇸", "birth": "1994.09.01", "story": "'레이스 교수'라는 별명에 걸맞은 뛰어난 전략 분석력의 완성형 드라이버입니다. 윌리엄스로 이적해 팀 전체의 체질을 바꾸는 구원투수로 활약 중입니다."},
            {"name_en": "Alexander Albon", "name_kr": "알렉산더 알본", "number": "23", "country": "태국 🇹🇭", "birth": "1996.03.23", "story": "어려운 머신으로 마법 같은 주행을 보여주어 '윌리엄스의 구세주'라 불립니다. 탁월한 타이어 세이브 능력으로 팀원들의 신뢰를 한몸에 받습니다."}
        ]
    },
    {
        "team_en": "Aston Martin Aramco F1 Team", "team_kr": "애스턴 마틴", "color": "#229971", "principal": "Andy Cowell", "power_unit": "Honda",
        "drivers": [
            {"name_en": "Fernando Alonso", "name_kr": "페르난도 알론소", "number": "14", "country": "스페인 🇪🇸", "birth": "1981.07.29", "story": "나이를 거꾸로 먹는 듯한 반사 신경과 맹수 같은 시야를 지닌 불멸의 전설입니다. 수십 년 커리어의 노하우를 동원해 팀의 최상위권 도약을 이끕니다."},
            {"name_en": "Lance Stroll", "name_kr": "랜스 스트롤", "number": "18", "country": "캐나다 🇨🇦", "birth": "1998.10.29", "story": "비가 내리는 악천후 서킷이나 예측 불가능한 혼전 상황에서 유독 빛을 발합니다. 결정적인 순간마다 예리한 추월을 성공시키는 소유자입니다."}
        ]
    },
    {
        "team_en": "Cadillac F1 Team", "team_kr": "캐딜락 F1 팀", "color": "#FFD700", "principal": "Graeme Lowdon", "power_unit": "Ferrari",
        "drivers": [
            {"name_en": "Valtteri Bottas", "name_kr": "발테리 보타스", "number": "77", "country": "핀란드 🇫🇮", "birth": "1989.08.28", "story": "통산 10회 우승을 기록한 메르세데스 전성기의 주역입니다. 풍부한 개발 경험으로 신생 캐딜락 팀의 머신 셋업 기준점을 제시합니다."},
            {"name_en": "Sergio Pérez", "name_kr": "세르히오 페레스", "number": "11", "country": "멕시코 🇲🇽", "birth": "1990.01.26", "story": "시가지 서킷의 마법사라 불리며 환상적인 타이어 관리 능력을 지닌 멕시코의 영웅입니다. 노련한 레이스 운영으로 캐딜락 팀의 안착을 돕습니다."}
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

# 세션 상태 초기화
if "selected_driver" not in st.session_state:
    st.session_state.selected_driver = None

# 탭 메뉴 구성
tab1, tab2 = st.tabs(["🔍 F1 팀 검색 및 선수 정보", "📅 2026 그랑프리 일정 & 포디움"])

# [탭 1] 팀 검색 및 선수 클릭 기능
with tab1:
    st.subheader("🔍 F1 팀 검색 및 소속 선수 심층 정보")
    st.write("아래에서 팀을 고르신 뒤, 보고 싶은 **선수의 이름 버튼**을 누르면 상세한 서사와 프로필이 나타납니다.")
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
            
            st.markdown("### 👥 소속 드라이버 (버튼을 누르면 아래에 설명이 나타납니다)")
            d_cols = st.columns(2)
            
            for idx, driver in enumerate(team["drivers"]):
                with d_cols[idx]:
                    btn_label = f"#{driver['number']} {driver['name_kr']} ({driver['name_en']})"
                    if st.button(btn_label, key=f"btn_{driver['number']}_{driver['name_en']}"):
                        st.session_state.selected_driver = driver

    if st.session_state.selected_driver:
        d = st.session_state.selected_driver
        st.markdown("---")
        st.markdown(f"""
            <div class="driver-detail-box">
                <h3 style="color: #ff4d4d; margin-top: 0; font-family: 'Orbitron', sans-serif;">🏁 #{d['number']} {d['name_kr']} ({d['name_en']}) 심층 프로필</h3>
                <p style="margin: 6px 0; font-size: 1.05rem;"><b>국적:</b> {d['country']}</p>
                <p style="margin: 6px 0; font-size: 1.05rem;"><b>생년월일:</b> {d['birth']}</p>
                <hr style="border-color: rgba(255,255,255,0.15); margin: 12px 0;">
                <p style="font-size: 1.1rem; line-height: 1.6; color: #e2e8f0; margin-bottom: 0;">
                    <b>드라이버 서사:</b> {d['story']}
                </p>
            </div>
        """, unsafe_allow_html=True)

# [탭 2] 2026 그랑프리 일정표 및 포디움 결과
with tab2:
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
