import streamlit as st
from datetime import datetime

# 1. 페이지 기본 설정
st.set_page_config(
    page_title="F1ow - Formula 1 Fan Hub",
    page_icon="🏎️",
    layout="wide"
)

# 2. 가독성 최적화 및 F1 테마 CSS 스타일링
st.markdown("""
    <style>
    /* 전체 배경 스타일 - 딥 다크 모드 */
    .stApp {
        background-color: #0b0e14;
    }
    
    /* 기본 글자색 설정 */
    html, body, [class*="css"], p, span, div, h1, h2, h3, h4, h5, h6 {
        color: #FFFFFF;
    }

    /* 드롭다운(selectbox) 검색창 글씨 및 배경색 고침 - 검은색 글씨로 시독성 확보 */
    div[data-baseweb="select"] {
        background-color: #ffffff !important;
        border-radius: 8px !important;
    }
    div[data-baseweb="select"] * {
        color: #000000 !important;
        font-weight: bold !important;
    }
    div[data-baseweb="popover"] * {
        color: #000000 !important;
        background-color: #ffffff !important;
    }
    li[role="option"]:hover {
        background-color: #e0e0e0 !important;
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
        background: linear-gradient(90deg, #161b22 0%, #0b0e14 50%, #161b22 100%);
        border-radius: 12px;
    }
    .f1ow-text {
        color: #E10600 !important;
        font-size: 3.5rem;
        font-weight: 900;
        letter-spacing: 4px;
        font-family: 'Arial Black', sans-serif;
        text-shadow: 0 0 15px rgba(225, 6, 0, 0.5);
    }
    .f1ow-sub {
        color: #FFFFFF !important;
        font-size: 1.2rem;
        letter-spacing: 2px;
        font-weight: bold;
    }

    /* 서브 타이틀 */
    .sub-title {
        color: #FFFFFF !important;
        border-left: 5px solid #E10600;
        padding-left: 12px;
        font-size: 1.5rem;
        font-weight: bold;
        margin-bottom: 20px;
        letter-spacing: 1px;
    }

    /* 팀 정보 전용 카본 카드 (사진 제거 버전) */
    .team-info-card {
        background: linear-gradient(145deg, #1c2128 0%, #13171d 100%);
        padding: 25px;
        border-radius: 15px;
        border: 1px solid #30363d;
        border-left: 6px solid #E10600;
        box-shadow: 0 8px 24px rgba(0,0,0,0.6);
        margin-bottom: 20px;
    }
    
    .team-title-tag {
        font-size: 2rem;
        font-weight: 900;
        color: #E10600 !important;
        margin-bottom: 10px;
        letter-spacing: 1px;
    }

    /* 드라이버 Expander(아코디언) 가독성 최적화 */
    .driver-box {
        background-color: #161b22;
        border-radius: 10px;
        border: 1px solid #30363d;
        padding: 15px;
        margin-bottom: 15px;
    }

    /* 스케줄 그랑프리 카드 디자인 (F1 레이싱 느낌) */
    .gp-card {
        background: linear-gradient(135deg, #161b22 0%, #0d1117 100%);
        border: 1px solid #30363d;
        border-radius: 12px;
        padding: 18px 22px;
        margin-bottom: 15px;
        transition: all 0.2s ease-in-out;
        position: relative;
        overflow: hidden;
    }
    .gp-card.completed {
        border-left: 6px solid #484f58;
        opacity: 0.75;
    }
    .gp-card.next-race {
        border-left: 6px solid #E10600;
        background: linear-gradient(135deg, #221013 0%, #0d1117 100%);
        box-shadow: 0 0 15px rgba(225, 6, 0, 0.3);
    }
    .gp-card.upcoming {
        border-left: 6px solid #238636;
    }

    /* 상태 태그 (뱃지) */
    .status-badge {
        display: inline-block;
        padding: 4px 10px;
        border-radius: 20px;
        font-size: 0.8rem;
        font-weight: bold;
        letter-spacing: 1px;
        margin-bottom: 8px;
    }
    .badge-completed {
        background-color: #30363d;
        color: #8b949e !important;
    }
    .badge-next {
        background-color: #E10600;
        color: #FFFFFF !important;
        animation: pulse 2s infinite;
    }
    .badge-upcoming {
        background-color: #238636;
        color: #FFFFFF !important;
    }

    .gp-round {
        font-size: 0.9rem;
        font-weight: 800;
        color: #E10600 !important;
        letter-spacing: 1px;
    }
    .gp-title {
        font-size: 1.4rem;
        font-weight: 800;
        color: #FFFFFF !important;
        margin: 4px 0;
    }
    .gp-circuit {
        font-size: 0.95rem;
        color: #8b949e !important;
    }
    .gp-date {
        font-size: 1rem;
        font-weight: bold;
        color: #f0f6fc !important;
    }

    /* Session timeline box */
    .session-box {
        background-color: #0d1117;
        border-radius: 8px;
        padding: 12px;
        margin-top: 10px;
        border: 1px solid #21262d;
    }
    </style>
""", unsafe_allow_html=True)

# 3. F1 팀 및 드라이버 데이터 (이미지 경로/태그 전면 제거)
F1_TEAMS = {
    "레드불 (Red Bull Racing)": {
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

# 4. 2026 시즌 일정표 데이터 (현재 시점 2026년 9월 초 기준 종료 여부 적용)
# 8월 말까지 (ROUND 01 ~ ROUND 12) 진행 완료
F1_SCHEDULE_KOREAN = [
    {"round": "ROUND 01", "gp": "🇦🇺 호주 그랑프리", "circuit": "알버트 파크 서킷 (멜버른)", "date": "3월 6일 - 3월 8일", "status": "COMPLETED"},
    {"round": "ROUND 02", "gp": "🇨🇳 중국 그랑프리", "circuit": "상하이 인터내셔널 서킷", "date": "3월 13일 - 3월 15일", "status": "COMPLETED"},
    {"round": "ROUND 03", "gp": "🇯🇵 일본 그랑프리", "circuit": "스즈카 서킷", "date": "3월 27일 - 3월 29일", "status": "COMPLETED"},
    {"round": "ROUND 04", "gp": "🇺🇸 마이애미 그랑프리", "circuit": "마이애미 인터네셔널 오토드롬", "date": "5월 1일 - 5월 3일", "status": "COMPLETED"},
    {"round": "ROUND 05", "gp": "🇨🇦 캐나다 그랑프리", "circuit": "질 빌뇌브 서킷", "date": "5월 22일 - 5월 24일", "status": "COMPLETED"},
    {"round": "ROUND 06", "gp": "🇲🇨 모나코 그랑프리", "circuit": "서킷 드 모나코 (몬테카를로)", "date": "6월 5일 - 6월 7일", "status": "COMPLETED"},
    {"round": "ROUND 07", "gp": "🇪🇸 스페인 바르셀로나 GP", "circuit": "서킷 드 바르셀로나-카탈루냐", "date": "6월 12일 - 6월 14일", "status": "COMPLETED"},
    {"round": "ROUND 08", "gp": "🇦🇹 오스트리아 그랑프리", "circuit": "레드불 링 (슈필베르크)", "date": "6월 26일 - 6월 28일", "status": "COMPLETED"},
    {"round": "ROUND 09", "gp": "🇬🇧 영국 그랑프리", "circuit": "실버스톤 서킷", "date": "7월 3일 - 7월 5일", "status": "COMPLETED"},
    {"round": "ROUND 10", "gp": "🇧🇪 벨기에 그랑프리", "circuit": "스파-프랑코샹 서킷", "date": "7월 17일 - 7월 19일", "status": "COMPLETED"},
    {"round": "ROUND 11", "gp": "🇭🇺 헝가리 그랑프리", "circuit": "헝가로링 (부다페스트)", "date": "7월 24일 - 7월 26일", "status": "COMPLETED"},
    {"round": "ROUND 12", "gp": "🇳🇱 네덜란드 그랑프리", "circuit": "잔트보르트 서킷", "date": "8월 21일 - 8월 23일", "status": "COMPLETED"},
    {"round": "ROUND 13", "gp": "🇮🇹 이탈리아 몬차 GP", "circuit": "몬차 국립 서킷", "date": "9월 4일 - 9월 6일", "status": "NEXT_RACE"},
    {"round": "ROUND 14", "gp": "🇪🇸 마드리드 그랑프리", "circuit": "마드리드 스트리트 서킷", "date": "9월 11일 - 9월 13일", "status": "UPCOMING"},
    {"round": "ROUND 15", "gp": "🇦🇿 아제르바이젠 GP", "circuit": "바쿠 시티 서킷", "date": "9월 24일 - 9월 26일", "status": "UPCOMING"},
    {"round": "ROUND 16", "gp": "🇸🇬 싱가포르 그랑프리", "circuit": "마리나 베이 스트리트 서킷", "date": "10월 9일 - 10월 11일", "status": "UPCOMING"},
    {"round": "ROUND 17", "gp": "🇺🇸 미국 COTA GP", "circuit": "서킷 오브 디 아메리카스", "date": "10월 23일 - 10월 25일", "status": "UPCOMING"},
    {"round": "ROUND 18", "gp": "🇲🇽 멕시코 그랑프리", "circuit": "아우토드로모 에르마노스 로드리게스", "date": "10월 30일 - 11월 1일", "status": "UPCOMING"},
    {"round": "ROUND 19", "gp": "🇧🇷 브라질 상파울루 GP", "circuit": "인테르라고스 서킷", "date": "11월 6일 - 11월 8일", "status": "UPCOMING"},
    {"round": "ROUND 20", "gp": "🇺🇸 라스베이거스 GP", "circuit": "라스베이거스 스트립 서킷", "date": "11월 19일 - 11월 21일", "status": "UPCOMING"},
    {"round": "ROUND 21", "gp": "🇶🇦 카타르 그랑프리", "circuit": "루사일 인터내셔널 서킷", "date": "11월 27일 - 11월 29일", "status": "UPCOMING"},
    {"round": "ROUND 22", "gp": "🇦🇪 아부다비 그랑프리", "circuit": "야스 마리나 서킷", "date": "12월 4일 - 12월 6일", "status": "UPCOMING"}
]

# 상단 텍스트 전용 헤더 (사진 제거)
st.markdown("""
    <div class="header-container">
        <span class="f1ow-text">🏎️ F1ow</span>
        <span class="f1ow-sub">| FORMULA 1 FAN HUB</span>
    </div>
""", unsafe_allow_html=True)

# 탭 메뉴
tab1, tab2 = st.tabs(["🏎️ 팀 & 드라이버 검색", "📅 2026 그랑프리 레이스 일정표"])

# [TAB 1] 팀 정보 & 드라이버 라인업 (검색 글씨 검은색 처리 완료 & 사진 제거)
with tab1:
    st.markdown('<div class="sub-title">F1 팀 정보 및 소속 드라이버 조회</div>', unsafe_allow_html=True)
    
    # 드롭다운 선택창 (CSS로 선택창 내부 글씨 검은색 강제)
    selected_team = st.selectbox("조회할 팀을 선택하세요 (팀 이름 선택):", list(F1_TEAMS.keys()))
    
    if selected_team:
        team = F1_TEAMS[selected_team]
        
        st.markdown(f"""
            <div class="team-info-card">
                <div class="team-title-tag">🏁 {selected_team}</div>
                <p style="font-size: 1.1rem; margin-bottom: 8px;"><b>🗓️ 창단 연도:</b> {team['founded']}</p>
                <p style="font-size: 1.1rem; margin-bottom: 12px;"><b>📍 팀 본거지:</b> {team['base']}</p>
                <div style="background-color: #21262d; padding: 15px; border-radius: 8px; border-left: 4px solid #E10600;">
                    <p style="margin:0; font-size: 1.05rem; line-height: 1.5;"><b>💡 팀 스토리 & 특징:</b><br>{team['features']}</p>
                </div>
            </div>
        """, unsafe_allow_html=True)
        
        st.markdown("### 👨‍✈️ 소속 드라이버 라인업")
        
        col1, col2 = st.columns(2)
        for idx, driver in enumerate(team["drivers"]):
            target_col = col1 if idx == 0 else col2
            with target_col:
                st.markdown(f"""
                    <div class="driver-box">
                        <h4 style="color:#E10600; margin-top:0;">🏎️ Car No. {driver['no']}</h4>
                        <h3 style="color:#FFFFFF; margin-bottom:10px;">{driver['name']}</h3>
                        <p style="margin-bottom:6px;"><b>🚩 국적:</b> {driver['country']}</p>
                        <hr style="border-color:#30363d;">
                        <p style="font-size:0.95rem; line-height:1.4; color:#c9d1d9;">{driver['bio']}</p>
                    </div>
                """, unsafe_allow_html=True)

# [TAB 2] 멋진 F1 느낌의 일정표 (종료된 경기 표시 기능 추가)
with tab2:
    st.markdown('<div class="sub-title">2026 시즌 그랑프리 레이스 스케줄</div>', unsafe_allow_html=True)
    
    # 상단 요약 카운터
    completed_count = sum(1 for item in F1_SCHEDULE_KOREAN if item["status"] == "COMPLETED")
    total_count = len(F1_SCHEDULE_KOREAN)
    
    col_stat1, col_stat2, col_stat3 = st.columns(3)
    col_stat1.metric("🏁 총 그랑프리", f"{total_count} 레이스")
    col_stat2.metric("✅ 진행 완료 경기", f"{completed_count} 경기", delta="종료됨")
    col_stat3.metric("⚡ 남은 그랑프리", f"{total_count - completed_count} 경기")
    
    st.markdown("---")
    
    # 레이스 일정 목록
    for item in F1_SCHEDULE_KOREAN:
        status_class = "completed" if item["status"] == "COMPLETED" else ("next-race" if item["status"] == "NEXT_RACE" else "upcoming")
        
        if item["status"] == "COMPLETED":
            badge_html = '<span class="status-badge badge-completed">🏁 경기 종료 (COMPLETED)</span>'
        elif item["status"] == "NEXT_RACE":
            badge_html = '<span class="status-badge badge-next">⚡ NEXT RACE (다음에 열릴 경기)</span>'
        else:
            badge_html = '<span class="status-badge badge-upcoming">🟢 예정 (UPCOMING)</span>'

        with st.container():
            st.markdown(f"""
                <div class="gp-card {status_class}">
                    <div>
                        {badge_html}
                        <div class="gp-round">{item['round']}</div>
                        <div class="gp-title">{item['gp']}</div>
                        <div class="gp-circuit">📍 {item['circuit']}</div>
                        <div class="gp-date">🗓️ {item['date']}</div>
                    </div>
                </div>
            """, unsafe_allow_html=True)
            
            with st.expander(f"⏱️ {item['gp']} 상세 주말 세션 스케줄 확인"):
                st.markdown(f"""
                    <div class="session-box">
                        <p style="color:#E10600; font-weight:bold; margin-bottom:8px;">📌 세션 일정 가이드</p>
                        <p style="margin-bottom:4px;">• <b>금요일:</b> 자유 연습 세션 (FP1 / FP2)</p>
                        <p style="margin-bottom:4px;">• <b>토요일:</b> 자유 연습 (FP3) & 예선전 (Qualifying)</p>
                        <p style="margin-bottom:0;">• <b>일요일:</b> <b>🔥 결승 메인 레이스 (Grand Prix Race)</b></p>
                    </div>
                """, unsafe_allow_html=True)
