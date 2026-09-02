from datetime import datetime
import pandas as pd
import streamlit as st

# 페이지 설정
st.set_page_config(
    page_title="2026 FORMULA 1",
    page_icon="🏎️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Custom CSS (다크 매트 블랙 + F1 시그니처 레드 스타일링)
st.markdown(
    """
    <style>
    /* 전체 배경 매트 블랙 */
    .stApp {
        background-color: #0b0b0e;
        color: #ffffff;
    }
    
    /* 사이드바 스타일링 */
    [data-testid="stSidebar"] {
        background-color: #121216;
        border-right: 1px solid #22222a;
    }

    /* 텍스트 색상 및 글로벌 서식 강제 하얀색 */
    h1, h2, h3, h4, h5, h6, p, span, label, div {
        color: #ffffff !important;
    }

    /* F1 메인 로고 및 헤더 */
    .main-header {
        text-align: center;
        padding: 10px 0 20px 0;
    }
    
    /* 카드 디자인 */
    .f1-card {
        background: linear-gradient(135deg, #16161c 0%, #0d0d11 100%);
        border-radius: 12px;
        padding: 24px;
        margin-bottom: 25px;
        border-left: 6px solid #e10600;
        box-shadow: 0 8px 16px rgba(225, 6, 0, 0.15);
    }

    /* 드라이버 명함 카드 */
    .driver-card {
        background-color: #1a1a22;
        border: 1px solid #2e2e3a;
        border-radius: 10px;
        padding: 15px 20px;
        margin-bottom: 10px;
        border-top: 3px solid #e10600;
    }

    /* 검색창 스타일 */
    .stTextInput input {
        background-color: #1a1a24 !important;
        color: #ffffff !important;
        border: 1px solid #333344 !important;
        border-radius: 8px !important;
    }
    .stTextInput input:focus {
        border-color: #e10600 !important;
        box-shadow: 0 0 8px rgba(225, 6, 0, 0.5) !important;
    }

    /* 일정표 아이템 스타일 */
    .schedule-item {
        background-color: #161620;
        border-radius: 10px;
        padding: 15px 20px;
        margin-bottom: 12px;
        border-left: 4px solid #e10600;
        display: flex;
        align-items: center;
        justify-content: space-between;
    }
    .status-completed {
        color: #4CAF50 !important;
        font-weight: bold;
    }
    .status-upcoming {
        color: #FF9800 !important;
        font-weight: bold;
    }
    </style>
""",
    unsafe_allow_html=True,
)

# ---------------------------------------------------------
# F1 Header Logo & Title
# ---------------------------------------------------------
st.markdown('<div class="main-header">', unsafe_allow_html=True)
st.image(
    "https://upload.wikimedia.org/wikipedia/commons/3/33/F1.svg", width=320
)
st.markdown(
    "<h1 style='text-align: center; font-size: 2.8rem; font-weight: 900; letter-spacing: 2px; color: #ffffff;'>2026 FORMULA 1</h1>",
    unsafe_allow_html=True,
)
st.markdown("</div>", unsafe_allow_html=True)
st.divider()

# ---------------------------------------------------------
# Data Definition & Search Mapping
# ---------------------------------------------------------
team_aliases = {
    "Red Bull Racing": [
        "redbull",
        "red bull",
        "레드불",
        "레드불 레이싱",
        "레드불레이싱",
    ],
    "Ferrari": ["ferrari", "페라리", "스쿠데리아"],
    "Mercedes": ["mercedes", "메르세데스", "벤츠", "메르세데스 벤츠"],
    "McLaren": ["mclaren", "맥라렌"],
    "Aston Martin": ["aston martin", "애스턴마틴", "애스턴 마틴", "아스톤마틴"],
    "Alpine": ["alpine", "알핀"],
    "Williams": ["williams", "윌리엄스"],
    "Racing Bulls": [
        "racing bulls",
        "레이싱불스",
        "레이싱 불스",
        "비자캐시앱",
        "rb",
    ],
    "Haas F1 Team": ["haas", "하스", "하스f1"],
    "Audi": ["audi", "아우디", "자우버"],
    "Cadillac F1 Team": ["cadillac", "캐딜락", "GM", "지엠"],
}

teams_data = {
    "Red Bull Racing": {
        "engine": "Red Bull Ford Powertrains",
        "base": "Milton Keynes, United Kingdom",
        "description": "2026년 파워유닛 대개혁에 맞춰 포드(Ford)와 손을 잡고 독자 파워유닛인 Red Bull Ford Powertrains를 도입한 레드불 레이싱입니다.",
        "drivers": [
            {
                "name": "막스 베르스타펜 (Max Verstappen)",
                "number": "3",
                "nationality": "네덜란드 🇳🇱",
                "short_desc": "현시대 F1을 지배하는 멀티 월드 챔피언",
                "long_desc": "막스 베르스타펜은 역대 최연소 F1 출전 및 우승 기록을 보유한 독보적인 에이스 드라이버입니다. 결단력 있는 추월과 완벽한 레이스 페이스를 자랑합니다.",
            },
            {
                "name": "아이작 하자르 (Isack Hadjar)",
                "number": "6",
                "nationality": "프랑스 🇫🇷",
                "short_desc": "레드불 주니어 출신의 공격적인 초신성 루키",
                "long_desc": "하위 카테고리에서 보여준 타협 없는 과감한 공격성과 짧은 브레이킹 존 활용 능력으로 크게 주목받은 유망주 드라이버입니다.",
            },
        ],
    },
    "Ferrari": {
        "engine": "Ferrari",
        "base": "Maranello, Italy",
        "description": "F1 출범 이래 단 한 번도 빠지지 않은 역사적 팀 스쿠데리아 페라리입니다.",
        "drivers": [
            {
                "name": "샤를 르클레르 (Charles Leclerc)",
                "number": "16",
                "nationality": "모나코 🇲🇨",
                "short_desc": "압도적인 퀄리파잉 스피드를 갖춘 페라리의 성골 에이스",
                "long_desc": "퀄리파잉 스피드 면에서 최고 수준으로 평가받는 드라이버로, 페라리에 대한 깊은 애정을 바탕으로 챔피언십에 도전합니다.",
            },
            {
                "name": "루이스 해밀턴 (Lewis Hamilton)",
                "number": "44",
                "nationality": "영국 🇬🇧",
                "short_desc": "F1 통산 7회 월드 챔피언이자 전설적인 살아있는 신화",
                "long_desc": "최다 우승, 최다 폴 포지션 기록을 보유하고 있으며, 페라리로 이적하여 통산 8번째 월드 타이틀을 노리고 있습니다.",
            },
        ],
    },
    "Mercedes": {
        "engine": "Mercedes",
        "base": "Brackley, United Kingdom",
        "description": "터보 하이브리드 시대를 지배했던 은빛 화살 메르세데스입니다.",
        "drivers": [
            {
                "name": "조지 러셀 (George Russell)",
                "number": "63",
                "nationality": "영국 🇬🇧",
                "short_desc": "정교함과 꾸준함을 겸비한 메르세데스의 1번 드라이버",
                "long_desc": "정밀한 엔지니어링 피드백과 높은 경기 운영 안정성이 무기인 드라이버입니다.",
            },
            {
                "name": "키미 안토넬리 (Kimi Antonelli)",
                "number": "12",
                "nationality": "이탈리아 🇮🇹",
                "short_desc": "차세대 챔피언으로 기대받는 이탈리아의 원더키드",
                "long_desc": "어린 나이에도 불구하고 코너링 진입 속도와 감각이 뛰어난 차세대 super-rookie입니다.",
            },
        ],
    },
    "McLaren": {
        "engine": "Mercedes",
        "base": "Woking, United Kingdom",
        "description": "완성도 높은 섀시 개발 능력을 바탕으로 최상위권으로 뛰어오른 전통의 명문 팀입니다.",
        "drivers": [
            {
                "name": "랜도 노리스 (Lando Norris)",
                "number": "1",
                "nationality": "영국 🇬🇧",
                "short_desc": "폭발적인 스피드의 맥라렌 대표 에이스",
                "long_desc": "완벽한 페이스 조절 능력과 휠-투-휠 배틀에서 최정상급 기량을 입증하고 있는 메인 드라이버입니다.",
            },
            {
                "name": "오스카 피아스트리 (Oscar Piastri)",
                "number": "81",
                "nationality": "호주 🇦🇺",
                "short_desc": "냉철한 판단력의 챔피언 재목",
                "long_desc": "압박감 속에서도 흔들림 없는 일명 'Ice Man' 스타일로 상위권 승부를 이어가고 있습니다.",
            },
        ],
    },
    "Aston Martin": {
        "engine": "Honda",
        "base": "Silverstone, United Kingdom",
        "description": "2026년부터 혼다와 독점 파트너십을 맺은 워크스 팀입니다.",
        "drivers": [
            {
                "name": "페르난도 알론소 (Fernando Alonso)",
                "number": "14",
                "nationality": "스페인 🇪🇸",
                "short_desc": "2회 월드 챔피언 출신 마스터 드라이버",
                "long_desc": "뛰어난 레이스 IQ와 탁월한 수비 스킬을 보여주는 베테랑 중의 베테랑입니다.",
            },
            {
                "name": "랜스 스트롤 (Lance Stroll)",
                "number": "18",
                "nationality": "캐나다 🇨🇦",
                "short_desc": "빗길 레이스 강자",
                "long_desc": "웨트 노면 등 난건 조건에서 빠른 반응 속도와 공격적인 스타트를 자랑합니다.",
            },
        ],
    },
    "Alpine": {
        "engine": "Mercedes",
        "base": "Enstone, United Kingdom",
        "description": "새로운 기술 구조 개편을 단행하여 중위권 선두를 노리는 팀입니다.",
        "drivers": [
            {
                "name": "피에르 개슬리 (Pierre Gasly)",
                "number": "10",
                "nationality": "프랑스 🇫🇷",
                "short_desc": "그랑프리 우승자 테크니션",
                "long_desc": "정교한 차량 세팅 피드백과 타이어 관리 능력이 특징입니다.",
            },
            {
                "name": "프랑코 콜라핀토 (Franco Colapinto)",
                "number": "43",
                "nationality": "아르헨티나 🇦🇷",
                "short_desc": "남미의 패기 넘치는 신예",
                "long_desc": "시원시원한 코너링 진입과 자비 없는 추월 시도로 모터스포츠 팬들의 선택을 받았습니다.",
            },
        ],
    },
    "Williams": {
        "engine": "Mercedes",
        "base": "Grove, United Kingdom",
        "description": "대대적인 시설 확충으로 명가 부활을 이루어 가고 있는 윌리엄스입니다.",
        "drivers": [
            {
                "name": "알렉산더 알본 (Alex Albon)",
                "number": "23",
                "nationality": "태국 🇹🇭",
                "short_desc": "윌리엄스 재건의 핵심 드라이버",
                "long_desc": "극단적인 타이어 관리 주행 능력으로 깜짝 포인트 획득에 능합니다.",
            },
            {
                "name": "카를로스 사인츠 (Carlos Sainz)",
                "number": "55",
                "nationality": "스페인 🇪🇸",
                "short_desc": "지능적인 피트 전략 수립가",
                "long_desc": "레이스 도중 스스로 뛰어난 판단력을 내리는 똑똑한 베테랑 드라이버입니다.",
            },
        ],
    },
    "Racing Bulls": {
        "engine": "Red Bull Ford Powertrains",
        "base": "Faenza, Italy",
        "description": "젊고 역동적인 이탈리아 기반 파엔차 유닛 팀입니다.",
        "drivers": [
            {
                "name": "리암 로슨 (Liam Lawson)",
                "number": "30",
                "nationality": "뉴질랜드 🇳🇿",
                "short_desc": "배짱 두둑한 신성",
                "long_desc": "접전 상황에서 물러서지 않고 상대를 밀어붙이는 대담함이 매력입니다.",
            },
            {
                "name": "아르비드 린드블라드 (Arvid Lindblad)",
                "number": "41",
                "nationality": "영국 🇬🇧",
                "short_desc": "레드불 주니어 초신성",
                "long_desc": "2026 규정 차체에 놀라운 적응력을 보이는 신인입니다.",
            },
        ],
    },
    "Haas F1 Team": {
        "engine": "Ferrari",
        "base": "Kannapolis, United States",
        "description": "미국 기반으로 페라리와 도요타 가주 레이싱의 지원을 받습니다.",
        "drivers": [
            {
                "name": "에스테반 오콘 (Esteban Ocon)",
                "number": "31",
                "nationality": "프랑스 🇫🇷",
                "short_desc": "철벽 디펜스의 대명사",
                "long_desc": "추격자를 확실히 따돌리는 철저한 블로킹 디펜스가 인상적입니다.",
            },
            {
                "name": "올리버 베어먼 (Oliver Bearman)",
                "number": "87",
                "nationality": "영국 🇬🇧",
                "short_desc": "영국의 차세대 라이징 스타",
                "long_desc": "데뷔전부터 대단한 성과를 거두며 기대를 이어가고 있는 스타입니다.",
            },
        ],
    },
    "Audi": {
        "engine": "Audi",
        "base": "Hinwil, Switzerland",
        "description": "독일 아우디가 자우버를 인수하여 만든 2026 신규 워크스 팀입니다.",
        "drivers": [
            {
                "name": "니코 휠켄베르크 (Nico Hülkenberg)",
                "number": "27",
                "nationality": "독일 🇩🇪",
                "short_desc": "아우디 프로젝트 테스터 베테랑",
                "long_desc": "한 랩의 한계치 성능을 이끌어 내는 베테랑 드라이버입니다.",
            },
            {
                "name": "가브리에우 보르툴레투 (Gabriel Bortoleto)",
                "number": "5",
                "nationality": "브라질 🇧🇷",
                "short_desc": "브라질 테크니션 신예",
                "long_desc": "하위 시리즈 연속 우승으로 완성도를 검증받은 유망주입니다.",
            },
        ],
    },
    "Cadillac F1 Team": {
        "engine": "Ferrari",
        "base": "Fishers, United States",
        "description": "GM 산하 11번째 새로 합류한 신생 팀 캐딜락입니다.",
        "drivers": [
            {
                "name": "세르히오 페레스 (Sergio Pérez)",
                "number": "11",
                "nationality": "멕시코 🇲🇽",
                "short_desc": "타이어 세이빙 마스터",
                "long_desc": "경기 후반 강력한 페이스 유지와 타이어 수명 관리의 귀재입니다.",
            },
            {
                "name": "발테리 보타스 (Valtteri Bottas)",
                "number": "77",
                "nationality": "핀란드 🇫🇮",
                "short_desc": "10회 이상 승리의 검증된 카드",
                "long_desc": "신생 팀이 빠르게 상위권 기준점에 진입하도록 중심을 잡아줍니다.",
            },
        ],
    },
}

schedule_data = [
    {
        "Round": 1,
        "Grand Prix": "호주 그랑프리",
        "Location": "🇦🇺 멜버른 (알버트 파크)",
        "Date": "2026-03-08",
    },
    {
        "Round": 2,
        "Grand Prix": "중국 그랑프리",
        "Location": "🇨🇳 상하이 (상하이 인터내셔널)",
        "Date": "2026-03-15",
    },
    {
        "Round": 3,
        "Grand Prix": "일본 그랑프리",
        "Location": "🇯🇵 스즈카 (스즈카 서킷)",
        "Date": "2026-03-29",
    },
    {
        "Round": 4,
        "Grand Prix": "마이애미 그랑프리",
        "Location": "🇺🇸 마이애미 (마이애미 오토드롬)",
        "Date": "2026-05-03",
    },
    {
        "Round": 5,
        "Grand Prix": "캐나다 그랑프리",
        "Location": "🇨🇦 몬트리올 (서킷 질 빌뇌브)",
        "Date": "2026-05-24",
    },
    {
        "Round": 6,
        "Grand Prix": "모나코 그랑프리",
        "Location": "🇲🇨 모나코 (서킷 드 모나코)",
        "Date": "2026-06-07",
    },
    {
        "Round": 7,
        "Grand Prix": "스페인 그랑프리",
        "Location": "🇪🇸 바르셀로나 (카탈루냐 서킷)",
        "Date": "2026-06-14",
    },
    {
        "Round": 8,
        "Grand Prix": "오스트리아 그랑프리",
        "Location": "🇦🇹 슈필베르크 (레드불 링)",
        "Date": "2026-06-28",
    },
    {
        "Round": 9,
        "Grand Prix": "영국 그랑프리",
        "Location": "🇬🇧 실버스톤 (실버스톤 서킷)",
        "Date": "2026-07-05",
    },
    {
        "Round": 10,
        "Grand Prix": "벨기에 그랑프리",
        "Location": "🇧🇪 스파 (스파-프랑코샹)",
        "Date": "2026-07-19",
    },
    {
        "Round": 11,
        "Grand Prix": "헝가리 그랑프리",
        "Location": "🇭🇺 부다페스트 (헝가로링)",
        "Date": "2026-07-26",
    },
    {
        "Round": 12,
        "Grand Prix": "네덜란드 그랑프리",
        "Location": "🇳🇱 잔트보르트 (잔트보르트 서킷)",
        "Date": "2026-08-23",
    },
    {
        "Round": 13,
        "Grand Prix": "이탈리아 그랑프리",
        "Location": "🇮🇹 몬자 (아우토드로모 몬자)",
        "Date": "2026-09-06",
    },
    {
        "Round": 14,
        "Grand Prix": "아제르바이잔 그랑프리",
        "Location": "🇦🇿 바쿠 (바쿠 시티 서킷)",
        "Date": "2026-09-20",
    },
    {
        "Round": 15,
        "Grand Prix": "싱가포르 그랑프리",
        "Location": "🇸🇬 싱가포르 (마리나 베이)",
        "Date": "2026-10-04",
    },
    {
        "Round": 16,
        "Grand Prix": "미국 그랑프리",
        "Location": "🇺🇸 오스틴 (COTA)",
        "Date": "2026-10-18",
    },
    {
        "Round": 17,
        "Grand Prix": "멕시코 그랑프리",
        "Location": "🇲🇽 멕시코시티 (에르마노스 로드리게스)",
        "Date": "2026-10-25",
    },
    {
        "Round": 18,
        "Grand Prix": "상파울루 그랑프리",
        "Location": "🇧🇷 상파울루 (인터라고스)",
        "Date": "2026-11-08",
    },
    {
        "Round": 19,
        "Grand Prix": "라스베이거스 그랑프리",
        "Location": "🇺🇸 라스베이거스 (스트리트 서킷)",
        "Date": "2026-11-21",
    },
    {
        "Round": 20,
        "Grand Prix": "카타르 그랑프리",
        "Location": "🇶🇦 루사일 (루사일 인터내셔널)",
        "Date": "2026-11-29",
    },
    {
        "Round": 21,
        "Grand Prix": "아부다비 그랑프리",
        "Location": "🇦🇪 아부다비 (야스 마리나)",
        "Date": "2026-12-06",
    },
]

# ---------------------------------------------------------
# Sidebar Navigation
# ---------------------------------------------------------
st.sidebar.title("🏁 MENU")
page = st.sidebar.radio(
    "이동할 페이지를 선택하세요:", ["팀 및 드라이버 검색", "2026 레이스 일정표"]
)

# ---------------------------------------------------------
# Page 1: Team Search & Drivers
# ---------------------------------------------------------
if page == "팀 및 드라이버 검색":
    st.subheader("🔍 F1 2026 팀 및 드라이버 검색")
    st.markdown(
        "<p style='color: #aaaaaa !important;'>팀명(예: 레드불, 메르세데스, 페라리, Red Bull 등)을 입력하면 관련 팀 정보가 표시됩니다.</p>",
        unsafe_allow_html=True,
    )

    search_input = st.text_input(
        "검색할 팀명을 입력하세요:", "", placeholder="예: 레드불, 페라리, 메르세데스..."
    ).strip()

    matched_teams = []
    if search_input:
        query_lower = search_input.lower()
        for official_name, aliases in team_aliases.items():
            if any(query_lower in alias.lower() for alias in aliases) or (
                query_lower in official_name.lower()
            ):
                matched_teams.append(official_name)

    if not search_input:
        st.info(
            "💡 검색창에 팀명을 입력해 주세요. (입력 시 해당 팀의 세부 정보와 드라이버 라인업이 펼쳐집니다)"
        )
    elif search_input and not matched_teams:
        st.error(f"'{search_input}' 에 대한 검색 결과가 없습니다.")
    else:
        for team_name in matched_teams:
            info = teams_data[team_name]
            st.markdown(
                f"""
                <div class="f1-card">
                    <h2 style="color: #ffffff !important; margin-bottom: 10px;">🏎️ {team_name}</h2>
                    <p style="font-size: 1.05rem;"><b>⚙️ 파워 유닛:</b> <span style="color: #e10600 !important;">{info['engine']}</span></p>
                    <p style="font-size: 1.05rem;"><b>📍 팀 베이스:</b> {info['base']}</p>
                    <hr style="border-color: #333344; margin: 15px 0;">
                    <p style="font-size: 1.0m; line-height: 1.6; color: #dddddd !important;">{info['description']}</p>
                </div>
                """,
                unsafe_allow_html=True,
            )

            st.markdown("### 🏎️ 2026 드라이버 라인업")
            for driver in info["drivers"]:
                with st.expander(
                    f"🏎️ **#{driver['number']} {driver['name']}** - {driver['short_desc']}",
                    expanded=False,
                ):
                    st.markdown(
                        f"""
                        <div class="driver-card">
                            <h4 style="color: #ffffff !important; margin-bottom: 8px;">#{driver['number']} {driver['name']}</h4>
                            <p style="color: #aaaaaa !important; margin-bottom: 12px;"><b>국적:</b> {driver['nationality']}</p>
                            <p style="line-height: 1.7; font-size: 0.98rem; color: #eeeeee !important;">{driver['long_desc']}</p>
                        </div>
                        """,
                        unsafe_allow_html=True,
                    )
            st.divider()

# ---------------------------------------------------------
# Page 2: Grand Prix Schedule (분리형 카드 레이아웃으로 오류 해결)
# ---------------------------------------------------------
else:
    st.subheader("📅 2026 F1 그랑프리 레이스 일정")

    today = datetime.now().date()

    # 상단 요약 카드
    completed_count = sum(
        1
        for r in schedule_data
        if datetime.strptime(r["Date"], "%Y-%m-%d").date() < today
    )
    total_count = len(schedule_data)

    m1, m2, m3 = st.columns(3)
    m1.metric("총 라운드", f"{total_count} GP")
    m2.metric("진행 완료", f"{completed_count} GP")
    m3.metric("남은 경기", f"{total_count - completed_count} GP")

    st.divider()

    # 테이블 겹침 오류를 완벽 방지하는 독립적인 리스트 레이아웃
    for race in schedule_data:
        race_date = datetime.strptime(race["Date"], "%Y-%m-%d").date()
        is_completed = race_date < today

        # 컬럼 분리로 가독성 확보
        col_round, col_gp, col_loc, col_date, col_status = st.columns(
            [1, 2, 3, 2, 1.5]
        )

        with col_round:
            st.markdown(f"**Round {race['Round']}**")

        with col_gp:
            st.markdown(f"🏎️ **{race['Grand Prix']}**")

        with col_loc:
            st.markdown(f"{race['Location']}")

        with col_date:
            st.markdown(f"📅 {race['Date']}")

        with col_status:
            if is_completed:
                st.markdown(
                    "<span class='status-completed'>✅ 종료됨</span>",
                    unsafe_allow_html=True,
                )
            else:
                st.markdown(
                    "<span class='status-upcoming'>🏁 예정됨</span>",
                    unsafe_allow_html=True,
                )

        st.markdown(
            "<hr style='border: 0; border-top: 1px solid #222230; margin: 8px 0;'>",
            unsafe_allow_html=True,
        )
