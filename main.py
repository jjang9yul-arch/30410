import streamlit as st

st.set_page_config(
    page_title="F1 2026 시즌 종합 정보 Hub",
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

    .f1-header {
        font-family: 'Orbitron', sans-serif;
        font-size: 2.2rem;
        font-weight: 900;
        text-align: center;
        background: linear-gradient(90deg, #ffffff, #e10600);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 25px;
    }

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
    </style>
""", unsafe_allow_html=True)

# 헤더
st.markdown('<div class="f1-header">🏎️ 2026 F1 WORLD CHAMPIONSHIP</div>', unsafe_allow_html=True)

# 데이터베이스
f1_database = [
    {
        "team_en": "McLaren Formula 1 Team", "team_kr": "맥라렌", "color": "#FF8000", "principal": "Andrea Stella", "power_unit": "Mercedes",
        "team_desc": "1963년 브루스 맥라렌이 창단한 전통의 명문 팀으로, F1 역사상 두 번째로 많은 컨스트럭터 우승 기록을 보유하고 있습니다. 뛰어난 차체 샤시 개발 능력과 유연한 경기 운영을 통해 최근 다시 최정상 레이스에 복귀하며 매 시즌 강력한 우승 후보로 활약하고 있습니다.",
        "drivers": [
            {"name_en": "Lando Norris", "name_kr": "랜도 노리스", "number": "1", "country": "영국", "birth": "1999.11.13", "role": "메인 드라이버", 
             "desc": "2019년 맥라렌을 통해 F1에 데뷔한 이후 팀의 리딩 드라이버로 성장한 선수입니다.\n정교한 퀄리파잉 스피드와 안정적인 레이스 페이스를 겸비하여 매 경기 포디움을 다툽니다.\n오랜 기간 맥라렌의 재건을 이끌어왔으며 마침내 챔피언십 타이틀을 다투는 위치에 올랐습니다.\n특유의 밝은 성격과 공격적인 브레이킹 테크닉으로 세계적으로 두터운 팬층을 보유하고 있습니다."},
            {"name_en": "Oscar Piastri", "name_kr": "오스카 피아스트리", "number": "81", "country": "호주", "birth": "2001.04.06", "role": "메인 드라이버", 
             "desc": "F3와 F2를 연속으로 제패하며 역대급 루키로 평가받으며 F1에 화려하게 입성했습니다.\n데뷔 첫해부터 스프린트 레이스 우승과 포디움 입성을 기록하며 놀라운 침착성을 보여주었습니다.\n압박감이 심한 상황에서도 흔들리지 않는 멘탈과 냉정한 레이스 운영이 최대 강점입니다.\n맥라렌의 장기적인 승리를 이끌 핵심 차세대 챔피언 후보로 꼽힙니다."}
        ]
    },
    {
        "team_en": "Scuderia Ferrari", "team_kr": "페라리", "color": "#E8002d", "principal": "Frédéric Vasseur", "power_unit": "Ferrari",
        "team_desc": "1950년 F1 출범 이래 단 한 시즌도 빠짐없이 참가한 유일한 팀이자 모터스포츠의 상징입니다. 이탈리아의 자부심을 대표하며, 파워유닛 자체 제작 기술력과 수많은 전설적 드라이버들을 배출한 명실상부 F1 역사 그 자체입니다.",
        "drivers": [
            {"name_en": "Charles Leclerc", "name_kr": "샤를 르클레르", "number": "16", "country": "모나코", "birth": "1997.10.16", "role": "메인 드라이버", 
             "desc": "페라리 드라이버 아카데미 출신으로, 모나코 출신 최초의 페라리 메인 드라이버입니다.\n단 한 바퀴에 모든 것을 쏟아붓는 폭발적인 퀄리파잉 원랩 스피드가 최대 무기입니다.\n팀에 대한 높은 애정으로 모나코 홈 그랑프리 우승 등 굵직한 기록들을 만들어냈습니다.\n페라리를 다시 세계 정상에 올리기 위해 공격적인 드라이빙 스타트를 유지하고 있습니다."},
            {"name_en": "Lewis Hamilton", "name_kr": "루이스 해밀턴", "number": "44", "country": "영국", "birth": "1985.01.07", "role": "메인 드라이버", 
             "desc": "F1 통산 7회 월드 챔피언, 최다 우승, 최다 폴 포지션 기록을 보유한 살아있는 전설입니다.\n메르세데스와의 장기 집권을 마치고 페라리로 전격 이적하며 모터스포츠 역사상 가장 큰 화제를 모았습니다.\n타이어 관리 능력과 빗길 레이스, 철저한 경기 리딩 능력은 여전히 세계 최고 수준입니다.\n페라리에서의 8번째 월드 챔피언 타이틀 획득이라는 대기록 도전에 나섰습니다."}
        ]
    },
    {
        "team_en": "Mercedes-AMG Petronas F1 Team", "team_kr": "메르세데스", "color": "#27F4D2", "principal": "Toto Wolff", "power_unit": "Mercedes",
        "team_desc": "하이브리드 터보 에라 도입 이후 8년 연속 컨스트럭터 챔피언을 달성한 21세기 최강의 팀입니다. 독보적인 엔진 파워유닛 기술력과 정교한 데이터 분석을 바탕으로 언제나 강력한 우승 전력을 유지하고 있습니다.",
        "drivers": [
            {"name_en": "George Russell", "name_kr": "조지 러셀", "number": "63", "country": "영국", "birth": "1998.02.15", "role": "메인 드라이버", 
             "desc": "메르세데스 주니어 프로그램 출신으로 윌리엄스에서의 수련을 거쳐 메인 시트를 획득했습니다.\n어려운 차량 조건 속에서도 꾸준히 포인트를 획득하는 높은 경기 집중력을 보여줍니다.\n기술적인 분석력이 매우 뛰어나 차체 셋업 개선에 핵심적인 역할을 수행합니다.\n팀의 새로운 리드 드라이버로서 메르세데스의 왕좌 되찾기에 앞장서고 있습니다."},
            {"name_en": "Kimi Antonelli", "name_kr": "키미 안토넬리", "number": "12", "country": "이탈리아", "birth": "2006.08.25", "role": "메인 드라이버", 
             "desc": "카팅 무대부터 하위 카테고리를 초속으로 평정한 이탈리아 출신의 슈퍼 루키입니다.\n메르세데스가 수년간 공들여 육성한 신성으로 엄청난 코너링 스피드를 자랑합니다.\n어린 나이에도 불구하고 정교한 차체 컨트롤 능력을 입증하여 정식 드라이버로 발탁되었습니다.\nF1에 새로운 바람을 일으킬 가장 기대를 모으는 유망주입니다."}
        ]
    },
    {
        "team_en": "Oracle Red Bull Racing", "team_kr": "레드불", "color": "#3671C6", "principal": "Christian Horner", "power_unit": "Honda RBPT",
        "team_desc": "에어로다이내믹의 거장 에드리안 뉴이의 설계와 과감한 레이싱 스피릿을 바탕으로 F1에 지각변동을 일으킨 팀입니다. 압도적인 피트스탑 속도와 한계에 도전하는 전략으로 다수의 챔피언십을 타이틀을 보유하고 있습니다.",
        "drivers": [
            {"name_en": "Max Verstappen", "name_kr": "막스 베르스타펜", "number": "33", "country": "네덜란드", "birth": "1997.09.30", "role": "메인 드라이버", 
             "desc": "역대 최연소 데뷔 및 우승 기록을 경신하며 F1의 시대를 새로 쓴 월드 챔피언입니다.\n타협 없는 공격적인 추월 방식과 한 치의 오차도 없는 압도적인 레이스 페이스를 보유하고 있습니다.\n어떠한 노면 환경에서도 최상의 스피드를 끌어내는 독보적인 드라이빙 감각을 보여줍니다.\n레드불 레이싱의 절대적인 에이스로서 연승 기록을 이어나가고 있습니다."},
            {"name_en": "Yuki Tsunoda", "name_kr": "츠노다 유키", "number": "22", "country": "일본", "birth": "2000.05.11", "role": "메인 드라이버", 
             "desc": "혼다 드라이버 육성 프로그램을 통해 성장하여 F1 무대에 성공적으로 안착한 선수입니다.\n작은 체구에서 나오는 과감한 숏 브레이킹 테크닉과 놀라운 코너 추월 능력이 강점입니다.\n시즌을 거듭할수록 감정 조절과 타이어 관리 능력이 크게 발전했다는 평가를 받습니다.\n레드불 레이싱 시트를 쟁취하며 아시아 드라이버의 새로운 역사를 쓰고 있습니다."}
        ]
    },
    {
        "team_en": "Cadillac F1 Team", "team_kr": "캐딜락 F1 팀", "color": "#FFD700", "principal": "Graeme Lowdon", "power_unit": "Ferrari",
        "team_desc": "미국 제너럴 모터스(GM)의 프리미엄 브랜드 캐딜락이 2026년 대대적인 규정 개정에 맞춰 F1에 새롭게 출사표를 던진 창단 팀입니다. 검증된 베테랑 드라이버 라인업과 강력한 파워유닛을 바탕으로 신생팀의 반란을 꿈꾸고 있습니다.",
        "drivers": [
            {"name_en": "Valtteri Bottas", "name_kr": "발테리 보타스", "number": "77", "country": "핀란드", "birth": "1989.08.28", "role": "메인 드라이버", 
             "desc": "메르세데스 시절 통산 10회 우승을 차지하며 팀의 5연속 컨스트럭터 우승에 기여한 베테랑입니다.\n날카로운 원랩 스피드와 정교한 차량 피드백 능력으로 신생 팀 개발에 최적화되어 있습니다.\n풍부한 경험을 바탕으로 캐딜락 F1 팀의 초기 차체 셋업 및 안정화 작업을 이끌고 있습니다.\n특유의 쿨한 성격과 안정감 있는 레이스 운용으로 팀의 중심을 잡아줍니다."},
            {"name_en": "Sergio Pérez", "name_kr": "세르히오 페레스", "number": "11", "country": "멕시코", "birth": "1990.01.26", "role": "메인 드라이버", 
             "desc": "시가가지 서킷의 제왕이라 불리며 통산 6회 우승을 기록한 남미를 대표하는 베테랑입니다.\n타이어 수명을 극도로 늘리는 독보적인 타이어 관리 능력으로 유명합니다.\n치열한 중위권 싸움에서 포디움을 끌어내는 탁월한 위기관리 능력을 자랑합니다.\n신생 캐딜락 팀에 합류하여 풍부한 경험을 바탕으로 실점 없는 포인트를 노립니다."}
        ]
    }
]

f1_schedule_2026 = [
    {"라운드": "1R", "국가": "🇦🇺 오스트레일리아", "서킷 명칭": "앨버트 파크 서킷", "도시": "멜버른", "결승 날짜": "2026. 03. 08"},
    {"라운드": "2R", "국가": "🇨🇳 중국", "서킷 명칭": "상하이 인터내셔널 서킷", "도시": "상하이", "결승 날짜": "2026. 03. 15"},
    {"라운드": "3R", "국가": "🇯🇵 일본", "서킷 명칭": "스즈카 서킷", "도시": "스즈카", "결승 날짜": "2026. 03. 29"},
    {"라운드": "4R", "국가": "🇺🇸 미국", "서킷 명칭": "마이애미 인터내셔널 오토드로름", "도시": "마이애미", "결승 날짜": "2026. 05. 03"},
    {"라운드": "5R", "국가": "🇨🇦 캐나다", "서킷 명칭": "서킷 질 빌뇌브", "도시": "몬트리올", "결승 날짜": "2026. 05. 24"},
    {"라운드": "6R", "국가": "🇲🇨 모나코", "서킷 명칭": "서킷 드 모나코", "도시": "몬테카를로", "결승 날짜": "2026. 06. 07"},
    {"라운드": "7R", "국가": "🇪🇸 스페인", "서킷 명칭": "서킷 드 바르셀로나-카탈루냐", "도시": "바르셀로나", "결승 날짜": "2026. 06. 14"},
    {"라운드": "8R", "국가": "🇦🇹 오스트리아", "서킷 명칭": "레드불 링", "도시": "슈필베르크", "결승 날짜": "2026. 06. 28"},
    {"라운드": "9R", "국가": "🇬🇧 영국", "서킷 명칭": "실버스톤 서킷", "도시": "실버스톤", "결승 날짜": "2026. 07. 05"},
    {"라운드": "10R", "국가": "🇧🇪 벨기에", "서킷 명칭": "스파-프랑코샹 서킷", "도시": "스파", "결승 날짜": "2026. 07. 19"},
    {"라운드": "11R", "국가": "🇭🇺 헝가리", "서킷 명칭": "헝가로링", "도시": "부다페스트", "결승 날짜": "2026. 07. 26"},
    {"라운드": "12R", "국가": "🇳🇱 네덜란드", "서킷 명칭": "잔트포르트 서킷", "도시": "잔트포르트", "결승 날짜": "2026. 08. 23"},
    {"라운드": "13R", "국가": "🇮🇹 이탈리아", "서킷 명칭": "오토드로모 나치오날레 몬차", "도시": "몬차", "결승 날짜": "2026. 09. 06"},
    {"라운드": "14R", "국가": "🇪🇸 스페인", "서킷 명칭": "마드리드 스트리트 서킷", "도시": "마드리드", "결승 날짜": "2026. 09. 13"},
    {"라운드": "15R", "국가": "🇦🇿 아제르바이잔", "서킷 명칭": "바쿠 시티 서킷", "도시": "바쿠", "결승 날짜": "2026. 09. 26"},
    {"라운드": "16R", "국가": "🇸🇬 싱가포르", "서킷 명칭": "마리나 베이 스트리트 서킷", "도시": "싱가포르", "결승 날짜": "2026. 10. 11"},
    {"라운드": "17R", "국가": "🇺🇸 미국", "서킷 명칭": "서킷 오브 디 아메리카스", "도시": "오스틴", "결승 날짜": "2026. 10. 25"},
    {"라운드": "18R", "국가": "🇲🇽 멕시코", "서킷 명칭": "오토드로모 에르마노스 로드리게스", "도시": "멕시코시티", "결승 날짜": "2026. 11. 01"},
    {"라운드": "19R", "국가": "🇧🇷 브라질", "서킷 명칭": "호세 카를로스 파체 서킷 (인터라고스)", "도시": "상파울루", "결승 날짜": "2026. 11. 08"},
    {"라운드": "20R", "국가": "🇺🇸 미국", "서킷 명칭": "라스베이거스 스트립 서킷", "도시": "라스베이거스", "결승 날짜": "2026. 11. 21"},
    {"라운드": "21R", "국가": "🇶🇦 카타르", "서킷 명칭": "루사일 인터내셔널 서킷", "도시": "루사일", "결승 날짜": "2026. 11. 29"},
    {"라운드": "22R", "국가": "🇦🇪 아랍에미리트", "서킷 명칭": "야스 마리나 서킷", "도시": "아부다비", "결승 날짜": "2026. 12. 06"}
]

# 탭 메뉴 구성
tab1, tab2 = st.tabs(["🏎️ F1 팀 & 드라이버", "📅 2026 경기 일정"])

# Tab 1: 팀 및 드라이버 정보
with tab1:
    team_names = [t["team_kr"] for t in f1_database]
    selected_team_name = st.selectbox("팀을 선택하세요", team_names)

    for team in f1_database:
        if team["team_kr"] == selected_team_name:
            # 팀 상단 헤더 카드
            st.markdown(f"""
                <div class="team-card" style="border-top: 5px solid {team['color']};">
                    <div class="team-title" style="color: {team['color']};">{team['team_en']} ({team['team_kr']})</div>
                    <div style="margin-top: 5px;">
                        <span class="stat-badge">팀 감독: {team['principal']}</span>
                        <span class="stat-badge">파워 유닛: {team['power_unit']}</span>
                    </div>
                </div>
            """, unsafe_allow_html=True)
            
            # 팀 소개글 (토글 열기)
            with st.expander(f"📖 {team['team_kr']} 팀 소개글 보기", expanded=True):
                st.write(team["team_desc"])
            
            st.write("")
            st.subheader("🏎️ 소속 드라이버 라인업")
            
            # 드라이버 카드를 Columns으로 배치
            cols = st.columns(len(team["drivers"]))
            for idx, driver in enumerate(team["drivers"]):
                with cols[idx]:
                    st.markdown(f"### **#{driver['number']} {driver['name_kr']}**")
                    st.caption(f"{driver['name_en']}")
                    st.write(f"**국적:** {driver['country']} | **생년월일:** {driver['birth']}")
                    
                    # 드라이버 클릭 시 팝오버로 상세 설명 (4줄) 제공
                    with st.popover(f"🏎️ #{driver['number']} 상세 프로필 보기", use_container_width=True):
                        st.markdown(f"#### #{driver['number']} {driver['name_kr']} ({driver['name_en']})")
                        st.divider()
                        # 줄바꿈 처리하여 4줄 분량 표현
                        for line in driver["desc"].split("\n"):
                            st.write(f"• {line}")

# Tab 2: 일정표
with tab2:
    st.subheader("🏁 2026 FIA F1 월드 챔피언십 공식 일정표")
    st.write("2026 시즌 개최되는 전체 그랑프리 일정입니다.")
    
    # 깔끔한 테이블 스타일링 적용
    st.dataframe(
        f1_schedule_2026,
        use_container_width=True,
        hide_index=True,
        column_config={
            "라운드": st.column_config.TextColumn("라운드", width="small"),
            "국가": st.column_config.TextColumn("개최국", width="medium"),
            "서킷 명칭": st.column_config.TextColumn("서킷 이름", width="large"),
            "도시": st.column_config.TextColumn("도시", width="medium"),
            "결승 날짜": st.column_config.TextColumn("결승일", width="medium"),
        }
    )
