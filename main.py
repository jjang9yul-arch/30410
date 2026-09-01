import streamlit as st

# 1. 페이지 기본 설정
st.set_page_config(
    page_title="F1ow - Formula 1 Fan Hub",
    page_icon="🏎️",
    layout="wide"
)

# 2. 가독성 최적화 CSS 스타일링
st.markdown("""
    <style>
    /* 전체 배경 스타일 */
    .stApp {
        background-color: #0b0e14;
    }
    
    /* 전체 글자색 흰색 강제 적용 */
    html, body, [class*="css"], p, span, label, div, h1, h2, h3, h4, h5, h6 {
        color: #FFFFFF !important;
    }

    /* 상단 F1ow 헤더 디자인 */
    .header-container {
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 15px;
        padding: 20px 0;
        border-bottom: 3px solid #E10600;
        margin-bottom: 30px;
    }
    .f1-logo-img {
        height: 55px;
    }
    .f1ow-text {
        color: #FFFFFF !important;
        font-size: 3.2rem;
        font-weight: 900;
        letter-spacing: 2px;
        font-family: 'Arial Black', sans-serif;
    }

    /* 서브 타이틀 */
    .sub-title {
        color: #FFFFFF !important;
        border-left: 5px solid #E10600;
        padding-left: 12px;
        font-size: 1.5rem;
        font-weight: bold;
        margin-bottom: 20px;
    }

    /* 팀 로고 전용 카드 */
    .team-logo-card {
        background: linear-gradient(135deg, #ffffff 0%, #e0e0e0 100%);
        padding: 25px;
        border-radius: 15px;
        display: flex;
        justify-content: center;
        align-items: center;
        box-shadow: 0 8px 20px rgba(225, 6, 0, 0.2);
        margin-bottom: 20px;
    }

    /* 팀 정보 박스 */
    .team-info-card {
        background: #161b22;
        padding: 20px;
        border-radius: 12px;
        border: 1px solid #30363d;
        box-shadow: 0 4px 12px rgba(0,0,0,0.5);
    }

    /* 드라이버 및 일정표 Expander(아코디언) 제목 글씨색 및 가독성 최적화 */
    .streamlit-expanderHeader p {
        color: #FFFFFF !important;
        font-weight: bold !important;
        font-size: 1.1rem !important;
    }
    .streamlit-expanderHeader {
        background-color: #21262d !important;
        border-radius: 8px !important;
        border: 1px solid #363b42 !important;
        border-left: 5px solid #E10600 !important;
    }
    .streamlit-expanderContent {
        background-color: #161b22 !important;
        border: 1px solid #30363d !important;
        border-top: none !important;
        border-bottom-left-radius: 8px !important;
        border-bottom-right-radius: 8px !important;
        padding: 15px !important;
    }
    </style>
""", unsafe_allow_html=True)

# 3. F1 팀 및 드라이버 데이터
F1_TEAMS = {
    "레드불 (Red Bull Racing)": {
        "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/15/Red_Bull_Racing_logo.svg/512px-Red_Bull_Racing_logo.svg.png",
        "founded": "2005년",
        "base": "영국 밀턴킨스",
        "features": "에어로다이내믹스 거장 에드리언 뉴이의 유산과 막강한 파워트레인을 바탕으로 2010년대 및 2020년대 초반 F1을 지배한 최정상 명문 팀입니다.",
        "drivers": [
            {
                "name": "막스 페르스타펜 (Max Verstappen)",
                "no": "1",
                "country": "네덜란드 🇳🇱",
                "bio": "F1 월드 챔피언 출신으로 역대 최연소 데뷔 및 최연소 그랑프리 우승 기록을 보유한 압도적인 테크니션입니다."
            },
            {
                "name": "이삭 하드자르 (Isack Hadjar)",
                "no": "6",
                "country": "프랑스 🇫🇷",
                "bio": "레드불 주니어 프로그램 출신의 신예 드라이버로, 공격적인 레이스 스타일로 주목받는 차세대 라이징 스타입니다."
            }
        ]
    },
    "페라리 (Scuderia Ferrari)": {
        "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d1/Ferrari-Logo.svg/380px-Ferrari-Logo.svg.png",
        "founded": "1929년 (F1 참가: 1950년)",
        "base": "이탈리아 마라넬로",
        "features": "F1 출범 첫해인 1950년부터 단 한 번도 빠짐없이 참가한 가장 오래되고 상징적인 붉은 전차 명문 팀입니다.",
        "drivers": [
            {
                "name": "샤를 르클레르 (Charles Leclerc)",
                "no": "16",
                "country": "모나코 🇲🇨",
                "bio": "페라리의 성골 드라이버이자 타의 추종을 불허하는 원랩 스피드를 자랑하는 예선(Qualifying)의 마술사입니다."
            },
            {
                "name": "루이스 해밀턴 (Lewis Hamilton)",
                "no": "44",
                "country": "영국 🇬🇧",
                "bio": "7회 월드 챔피언이자 역대 최다 우승 및 폴포지션 기록을 보유한 살아있는 전설. 페라리로 전격 이적했습니다."
            }
        ]
    },
    "맥라렌 (McLaren F1 Team)": {
        "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a2/McLaren_Racing_logo.svg/512px-McLaren_Racing_logo.svg.png",
        "founded": "1963년",
        "base": "영국 워킹",
        "features": "아일톤 세나, 알랭 프로스트 등 수많은 전설을 배출한 명가로, 유려한 섀시 개발 기술로 다시 챔피언십 정상권에 복귀했습니다.",
        "drivers": [
            {
                "name": "랜도 노리스 (Lando Norris)",
                "no": "4",
                "country": "영국 🇬🇧",
                "bio": "맥라렌의 프랜차이즈 스타 드라이버로, 뛰어난 레이스 페이스와 일관성을 갖춘 차세대 챔피언 후보입니다."
            },
            {
                "name": "오스카 피아스트리 (Oscar Piastri)",
                "no": "81",
                "country": "호주 🇦🇺",
                "bio": "하위 카테고리를 싹쓸이하고 F1에 데뷔한 침착하고 대담한 레이스 운용 능력을 자랑하는 최고 루키 출신입니다."
            }
        ]
    },
    "메르세데스 (Mercedes-AMG F1)": {
        "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/fb/Mercedes_AMG_Petronas_F1_Logo.svg/512px-Mercedes_AMG_Petronas_F1_Logo.svg.png",
        "founded": "1954년 (재창단: 2010년)",
        "base": "영국 브랙리",
        "features": "터보 하이브리드 시대(2014~2021)에 8년 연속 컨스트럭터 챔피언이라는 전무후무한 대기록을 작성한 기술력의 정점 팀입니다.",
        "drivers": [
            {
                "name": "조지 러셀 (George Russell)",
                "no": "63",
                "country": "영국 🇬🇧",
                "bio": "메르세데스 육성 출신으로 정교한 스피드 판단력과 견고한 주행을 선보이는 팀의 핵심 드라이버입니다."
            },
            {
                "name": "키미 안토넬리 (Andrea Kimi Antonelli)",
                "no": "12",
                "country": "이탈리아 🇮🇹",
                "bio": "압도적인 재능으로 월반을 거듭하며 메르세데스 메인 시트를 차지한 이탈리아의 초신성 드라이버입니다."
            }
        ]
    },
    "애스턴 마틴 (Aston Martin)": {
        "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/53/Aston_Martin_logo.svg/512px-Aston_Martin_logo.svg.png",
        "founded": "2021년",
        "base": "영국 실버스톤",
        "features": "영국의 럭셔리 브랜드 바탕 위에 최신 풍동 시설과 시설을 확충하며 대대적인 투자를 집행하고 있는 기대주 팀입니다.",
        "drivers": [
            {
                "name": "페르난도 알론소 (Fernando Alonso)",
                "no": "14",
                "country": "스페인 🇪🇸",
                "bio": "2회 월드 챔피언이자 베테랑. 철저한 자기관리와 압도적인 경기 읽기 능력으로 팬들을 사로잡습니다."
            },
            {
                "name": "랜스 스트롤 (Lance Stroll)",
                "no": "18",
                "country": "캐나다 🇨🇦",
                "bio": "우천 시 레이스(Wet Race)와 차트 스타트에서 뛰어난 순발력을 보여주는 팀의 주축 멤버입니다."
            }
        ]
    },
    "알핀 (Alpine F1 Team)": {
        "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7e/Alpine_F1_Team_Logo.svg/512px-Alpine_F1_Team_Logo.svg.png",
        "founded": "2021년 (전신: 르노 F1)",
        "base": "영국 엔스톤 / 프랑스 비리샤티용",
        "features": "프랑스 르노 그룹의 스포츠 브랜드 알핀을 대표하며, 견고한 섀시 및 워크스 인프라를 바탕으로 경쟁합니다.",
        "drivers": [
            {
                "name": "피에르 가스리 (Pierre Gasly)",
                "no": "10",
                "country": "프랑스 🇫🇷",
                "bio": "2020 이탈리아 GP 우승 경험을 보유한 드라이버로, 과감한 추월 능력이 돋보이는 프랑스의 자존심입니다."
            },
            {
                "name": "프랑코 콜라핀토 (Franco Colapinto)",
                "no": "43",
                "country": "아르헨티나 🇦🇷",
                "bio": "남미 출신의 열정 넘치는 레이서로, 빠른 적응력과 과감한 시도로 가치를 증명하고 있습니다."
            }
        ]
    },
    "윌리엄스 (Williams Racing)": {
        "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/82/Williams_Racing_2020_Logo.svg/512px-Williams_Racing_2020_Logo.svg.png",
        "founded": "1977년",
        "base": "영국 그로브",
        "features": "프랭크 윌리엄스 경에 의해 창단된 전통의 전설적 프라이비티어 팀으로, 과감한 체질 개선을 통해 명가 재건을 진행 중입니다.",
        "drivers": [
            {
                "name": "알렉산더 알본 (Alexander Albon)",
                "no": "23",
                "country": "태국 🇹🇭",
                "bio": "윌리엄스의 에이스로 뛰어난 타이어 관리와 차량의 한계를 끌어내는 섬세한 운전 감각이 특징입니다."
            },
            {
                "name": "카를로스 사인츠 (Carlos Sainz)",
                "no": "55",
                "country": "스페인 🇪🇸",
                "bio": "페라리를 거쳐 합류한 명석한 레이서. 공학적 이해도가 뛰어나 피트 전략 수립에 탁월합니다."
            }
        ]
    },
    "하스 (Haas F1 Team)": {
        "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d4/Haas_F1_Team_logo.svg/512px-Haas_F1_Team_logo.svg.png",
        "founded": "2016년",
        "base": "미국 카나폴리스",
        "features": "미국 자본 기반의 팀으로 페라리와의 기술 파트너십을 이용해 경량화 및 효율성 극대화를 추구하는 실속파 팀입니다.",
        "drivers": [
            {
                "name": "에스테반 오콘 (Esteban Ocon)",
                "no": "31",
                "country": "프랑스 🇫🇷",
                "bio": "철벽 수비와 강한 승부욕을 보여주는 드라이버로, GP 우승 경력을 바탕으로 하스의 리더로 합류했습니다."
            },
            {
                "name": "올리버 베어먼 (Oliver Bearman)",
                "no": "87",
                "country": "영국 🇬🇧",
                "bio": "페라리 아카데미 출신으로 긴급 대체 출전에서도 훌륭한 기량을 보이며 정식 시트를 획득한 특급 신인입니다."
            }
        ]
    },
    "레이싱 불스 (RB)": {
        "logo": "https://upload.wikimedia.org/wikipedia/en/thumb/a/a2/Racing_Bulls_logo.svg/512px-Racing_Bulls_logo.svg.png",
        "founded": "2006년",
        "base": "이탈리아 파엔차",
        "features": "레드불의 자매 팀으로서 차세대 챔피언 후보들을 육성하고 기량을 시험하는 핵심 기지 역할을 합니다.",
        "drivers": [
            {
                "name": "리암 로슨 (Liam Lawson)",
                "no": "30",
                "country": "뉴질랜드 🇳🇿",
                "bio": "대타 출전 때마다 강렬한 포인트 획득을 이뤄내며 실력을 입증한 자신감 넘치는 레이서입니다."
            },
            {
                "name": "아비드 리드블라드 (Arvid Lindblad)",
                "no": "41",
                "country": "영국 🇬🇧",
                "bio": "레드불 주니어 아카데미가 아끼는 영건으로, 빠르고 날카로운 코너링 능력이 장점입니다."
            }
        ]
    },
    "자우버 / 아우디 (Sauber / Audi)": {
        "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/92/Audi-Logo_2016.svg/512px-Audi-Logo_2016.svg.png",
        "founded": "1993년",
        "base": "스위스 힌빌",
        "features": "스위스 자우버 팀 기반 위에 독일 명문 아우디(Audi)의 인수가 완료되어 풀 워크스 팩토리 팀으로 거듭나고 있습니다.",
        "drivers": [
            {
                "name": "니코 휠켄베르크 (Nico Hülkenberg)",
                "no": "27",
                "country": "독일 🇩🇪",
                "bio": "베테랑 중의 베테랑. 안정적인 피드백과 예선 일관성이 매력적인 경험 풍부한 드라이버입니다."
            },
            {
                "name": "가브리엘 보르톨레토 (Gabriel Bortoleto)",
                "no": "5",
                "country": "브라질 🇧🇷",
                "bio": "F3, F2 무대를 제패하며 브라질 F1의 새로운 희망으로 떠오른 천재 루키 드라이버입니다."
            }
        ]
    }
}

# 4. 클릭 가능한 인터랙티브 한글 일정표 데이터
F1_SCHEDULE_KOREAN = [
    {"round": "ROUND 01", "gp": "🇦🇺 호주 그랑프리", "circuit": "알버트 파크 서킷 (멜버른)", "date": "3월 6일 - 3월 8일"},
    {"round": "ROUND 02", "gp": "🇨🇳 중국 그랑프리", "circuit": "상하이 인터내셔널 서킷", "date": "3월 13일 - 3월 15일"},
    {"round": "ROUND 03", "gp": "🇯🇵 일본 그랑프리", "circuit": "스즈카 서킷", "date": "3월 27일 - 3월 29일"},
    {"round": "ROUND 04", "gp": "🇺🇸 마이애미 그랑프리", "circuit": "마이애미 인터네셔널 오토드롬", "date": "5월 1일 - 5월 3일"},
    {"round": "ROUND 05", "gp": "🇨🇦 캐나다 그랑프리", "circuit": "질 빌뇌브 서킷", "date": "5월 22일 - 5월 24일"},
    {"round": "ROUND 06", "gp": "🇲🇨 모나코 그랑프리", "circuit": "서킷 드 모나코 (몬테카를로)", "date": "6월 5일 - 6월 7일"},
    {"round": "ROUND 07", "gp": "🇪🇸 스페인 바르셀로나 GP", "circuit": "서킷 드 바르셀로나-카탈루냐", "date": "6월 12일 - 6월 14일"},
    {"round": "ROUND 08", "gp": "🇦🇹 오스트리아 그랑프리", "circuit": "레드불 링 (슈필베르크)", "date": "6월 26일 - 6월 28일"},
    {"round": "ROUND 09", "gp": "🇬🇧 영국 그랑프리", "circuit": "실버스톤 서킷", "date": "7월 3일 - 7월 5일"},
    {"round": "ROUND 10", "gp": "🇧🇪 벨기에 그랑프리", "circuit": "스파-프랑코샹 서킷", "date": "7월 17일 - 7월 19일"},
    {"round": "ROUND 11", "gp": "🇭🇺 헝가리 그랑프리", "circuit": "헝가로링 (부다페스트)", "date": "7월 24일 - 7월 26일"},
    {"round": "ROUND 12", "gp": "🇳🇱 네덜란드 그랑프리", "circuit": "잔트보르트 서킷", "date": "8월 21일 - 8월 23일"},
    {"round": "ROUND 13", "gp": "🇮🇹 이탈리아 몬차 GP", "circuit": "몬차 국립 서킷", "date": "9월 4일 - 9월 6일"},
    {"round": "ROUND 14", "gp": "🇪🇸 마드리드 그랑프리", "circuit": "마드리드 스트리트 서킷", "date": "9월 11일 - 9월 13일"},
    {"round": "ROUND 15", "gp": "🇦🇿 아제르바이젠 GP", "circuit": "바쿠 시티 서킷", "date": "9월 24일 - 9월 26일"},
    {"round": "ROUND 16", "gp": "🇸🇬 싱가포르 그랑프리", "circuit": "마리나 베이 스트리트 서킷", "date": "10월 9일 - 10월 11일"},
    {"round": "ROUND 17", "gp": "🇺🇸 미국 COTA GP", "circuit": "서킷 오브 디 아메리카스", "date": "10월 23일 - 10월 25일"},
    {"round": "ROUND 18", "gp": "🇲🇽 멕시코 그랑프리", "circuit": "아우토드로모 에르마노스 로드리게스", "date": "10월 30일 - 11월 1일"},
    {"round": "ROUND 19", "gp": "🇧🇷 브라질 상파울루 GP", "circuit": "인테르라고스 서킷", "date": "11월 6일 - 11월 8일"},
    {"round": "ROUND 20", "gp": "🇺🇸 라스베이거스 GP", "circuit": "라스베이거스 스트립 서킷", "date": "11월 19일 - 11월 21일"},
    {"round": "ROUND 21", "gp": "🇶🇦 카타르 그랑프리", "circuit": "루사일 인터내셔널 서킷", "date": "11월 27일 - 11월 29일"},
    {"round": "ROUND 22", "gp": "🇦🇪 아부다비 그랑프리", "circuit": "야스 마리나 서킷", "date": "12월 4일 - 12월 6일"}
]

# 상단 헤더 (공식 F1 로고 + F1ow)
st.markdown("""
    <div class="header-container">
        <img class="f1-logo-img" src="https://upload.wikimedia.org/wikipedia/commons/3/33/F1.svg" alt="F1 Logo">
        <span class="f1ow-text">F1ow</span>
    </div>
""", unsafe_allow_html=True)

# 탭 메뉴
tab1, tab2 = st.tabs(["🏎️ 팀 & 드라이버 검색", "📅 2026 한글 일정표"])

# [TAB 1] 팀 정보 & 드라이버 라인업
with tab1:
    st.markdown('<div class="sub-title">F1 팀 정보 및 드라이버 조회</div>', unsafe_allow_html=True)
    
    selected_team = st.selectbox("조회할 팀을 선택하세요:", list(F1_TEAMS.keys()))
    
    if selected_team:
        team = F1_TEAMS[selected_team]
        
        col1, col2 = st.columns([1, 1.3])
        
        with col1:
            st.markdown(f"""
                <div class="team-logo-card">
                    <img src="{team['logo']}" style="max-width:100%; max-height:140px; object-fit:contain;">
                </div>
            """, unsafe_allow_html=True)
            
            st.markdown(f"""
                <div class="team-info-card">
                    <h3 style="color:#E10600 !important; margin-top:0; font-weight:bold;">{selected_team}</h3>
                    <p><b>🗓️ 창단 연도:</b> {team['founded']}</p>
                    <p><b>📍 본거지:</b> {team['base']}</p>
                    <hr style="border-color:#333;">
                    <p><b>💡 팀 특징:</b><br>{team['features']}</p>
                </div>
            """, unsafe_allow_html=True)
            
        with col2:
            st.markdown("### 👨‍✈️ 소속 드라이버 라인업")
            st.info("💡 **선수 이름을 누르시면 프로필 정보가 아래로 펼쳐집니다!**")
            
            # 선수 클릭 시 상세 내용 표출 (글씨 가독성 개선)
            for driver in team["drivers"]:
                expander_label = f"🏎️ No. {driver['no']} | {driver['name']}"
                with st.expander(expander_label, expanded=False):
                    st.markdown(f"**👤 선수 이름:** {driver['name']}")
                    st.markdown(f"**🚩 국적:** {driver['country']}")
                    st.markdown(f"**🏎️ 차량 번호:** Car No. {driver['no']}")
                    st.write("---")
                    st.markdown("**📝 드라이버 상세 설명:**")
                    st.write(driver["bio"])

# [TAB 2] 한글 일정표 (클릭 시 상세 내용 표출)
with tab2:
    st.markdown('<div class="sub-title">2026 시즌 레이스 전체 일정</div>', unsafe_allow_html=True)
    st.info("💡 **원하시는 그랑프리를 클릭하시면 서킷 정보와 상세 일정이 나타납니다!**")
    
    for item in F1_SCHEDULE_KOREAN:
        expander_title = f"{item['round']} | {item['gp']} ({item['date']})"
        with st.expander(expander_title, expanded=False):
            st.markdown(f"### {item['gp']}")
            st.markdown(f"**📍 서킷 위치:** {item['circuit']}")
            st.markdown(f"**🗓️ 경기 일정:** {item['date']}")
            st.markdown("""
                **⏱️ 주말 세션 스케줄:**
                - 금요일: 연습 경기 (Practice 1, Practice 2)
                - 토요일: 연습 경기 (Practice 3) / 예선전 (Qualifying)
                - 일요일: **메인 결승 레이스 (Grand Prix Race)**
            """)
