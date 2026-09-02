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
    
    /* 고급스러운 카본 블랙 카드 디자인 */
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

    /* 검색창 및 입력폼 스타일 */
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

    /* Expander 토글 스타일 */
    .streamlit-expanderHeader {
        background-color: #161620 !important;
        border-radius: 8px !important;
        border: 1px solid #2a2a38 !important;
    }

    /* 데이터프레임 다크모드 서식 */
    [data-testid="stDataFrame"] {
        background-color: #121218;
        border-radius: 10px;
        padding: 10px;
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
# 한글/영문 키워드 매핑 테이블
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
        "description": "2026년 파워유닛 대개혁에 맞춰 포드(Ford)와 손을 잡고 독자 파워유닛인 Red Bull Ford Powertrains를 도입한 레드불 레이싱입니다. 섀시 및 공기역학 설계의 명가로서 2026 새 규정 아래에서도 최고의 기술력을 입증하고자 합니다.",
        "drivers": [
            {
                "name": "막스 베르스타펜 (Max Verstappen)",
                "number": "3",
                "nationality": "네덜란드 🇳🇱",
                "short_desc": "현시대 F1을 지배하는 멀티 월드 챔피언",
                "long_desc": (
                    "막스 베르스타펜은 역대 최연소 F1 출전 및 우승 기록을 보유한 독보적인 에이스 드라이버입니다. "
                    "상상을 초월하는 결단력 있는 추월, 타이어 마모 상황에서도 흔들리지 않는 완벽한 레이스 페이스, "
                    "그리고 젖은 노면(Wet condition)에서의 압도적인 제어력을 자랑합니다. "
                    "2026년 레드불-포드 새로운 파워유닛 시대를 맞아 팀의 명확한 리더로서 차체를 극한까지 끌어올리는 주행을 보여줍니다."
                ),
            },
            {
                "name": "아이작 하자르 (Isack Hadjar)",
                "number": "6",
                "nationality": "프랑스 🇫🇷",
                "short_desc": "레드불 주니어 출신의 공격적인 초신성 루키",
                "long_desc": (
                    "아이작 하자르는 레드불 주니어 드라이버 프로그램을 거쳐 2026년 레드불 메인 시트를 꿰찬 유망주입니다. "
                    "하위 카테고리(F3, F2)에서 보여준 타협 없는 과감한 공격성과 짧은 브레이킹 존 활용 능력으로 큰 주목을 받았습니다. "
                    "베르스타펜 옆에서 빠르게 피드백을 수용하며 메인 팀의 든든한 득점원으로 성장하고 있습니다."
                ),
            },
        ],
    },
    "Ferrari": {
        "engine": "Ferrari",
        "base": "Maranello, Italy",
        "description": "1950년 F1 출범 이래 단 한 번도 빠지지 않은 유일한 역사적 팀 스쿠데리아 페라리입니다. 마라넬로에서 자체 제작한 2026 신규 파워유닛과 명문팀의 자부심을 바탕으로 다시 한 번 월드 챔피언 타이틀 탈환에 나섭니다.",
        "drivers": [
            {
                "name": "샤를 르클레르 (Charles Leclerc)",
                "number": "16",
                "nationality": "모나코 🇲🇨",
                "short_desc": "압도적인 퀄리파잉 스피드를 갖춘 페라리의 성골 에이스",
                "long_desc": (
                    "샤를 르클레르는 한 랩을 쥐어짜내는 퀄리파잉(Qualifying) 스피드 면에서 현 그리드 최고 수준으로 평가받는 드라이버입니다. "
                    "페라리 드라이버 아카데미 출신으로 팀에 대한 애정이 깊으며, 까다로운 스트리트 서킷(모나코, 바쿠 등)에서 강점을 발휘합니다. "
                    "2026년 차세대 차량 구조에서도 차체의限界 성능을 끌어내는 선천적인 감각을 증명하고 있습니다."
                ),
            },
            {
                "name": "루이스 해밀턴 (Lewis Hamilton)",
                "number": "44",
                "nationality": "영국 🇬🇧",
                "short_desc": "F1 통산 7회 월드 챔피언이자 전설적인 살아있는 신화",
                "long_desc": (
                    "루이스 해밀턴은 F1 역사상 최다 우승, 최다 폴 포지션 기록을 보유한 리빙 레전드입니다. "
                    "경기 전반을 읽는 뛰어난 전략적 안목과 스티어링 휠 조작 및 타이어 세이빙 능력은 세계 최고 수준입니다. "
                    "메르세데스를 떠나 페라리로 전격 이적하며, 커리어 마지막 임무로 페라리의 챔피언십 복귀와 본인의 8번째 타이틀을 노리고 있습니다."
                ),
            },
        ],
    },
    "Mercedes": {
        "engine": "Mercedes",
        "base": "Brackley, United Kingdom",
        "description": "하이브리드 시대를 연승으로 지배했던 실버 애로우(Silver Arrows) 메르세데스입니다. 2026년 전기 모터 비중이 급격히 높아진 친환경 연료 규정에 맞춰 정밀한 엔진 기술력을 전면에 내세우고 있습니다.",
        "drivers": [
            {
                "name": "조지 러셀 (George Russell)",
                "number": "63",
                "nationality": "영국 🇬🇧",
                "short_desc": "정교함과 꾸준함을 겸비한 메르세데스의 1번 드라이버",
                "long_desc": (
                    "조지 러셀은 엔지니어링 분석 능력과 세밀한 차체 피드백으로 정평이 난 드라이버입니다. "
                    "윌리엄스 시절부터 하위권 차량으로 깜짝 폴 포지션 및 포디움을 기록하며 실력을 입증했으며, "
                    "어떠한 혼란스러운 레이스 조건에서도 꾸준하게 상위권 포인트를 획득해내는 안정성이 가장 큰 무기입니다."
                ),
            },
            {
                "name": "키미 안토넬리 (Kimi Antonelli)",
                "number": "12",
                "nationality": "이탈리아 🇮🇹",
                "short_desc": "차세대 챔피언으로 기대받는 이탈리아의 원더키드",
                "long_desc": (
                    "키미 안토넬리는 주니어 카팅 및 하위 레이싱 시리즈를 초속으로 패스하며 F1에 직행한 신동입니다. "
                    "어린 나이에도 불구하고 코너링 진입 속도와 차체 밸런스 감각이 뛰어나 토토 볼프 감독의 두터운 신임을 받고 있습니다. "
                    "메르세데스의 차세대 에이스로서 급격한 성장세를 보여주고 있습니다."
                ),
            },
        ],
    },
    "McLaren": {
        "engine": "Mercedes",
        "base": "Woking, United Kingdom",
        "description": "최근 수년간 완성도 높은 섀시 업데이트와 팀 리빌딩을 성공시키며 그리드 최상위권으로 뛰어오른 전통의 명문 맥라렌입니다.",
        "drivers": [
            {
                "name": "랜도 노리스 (Lando Norris)",
                "number": "1",
                "nationality": "영국 🇬🇧",
                "short_desc": "폭발적인 스피드와 친근한 팬덤을 모두 갖춘 맥라렌의 에이스",
                "long_desc": (
                    "랜도 노리스는 오랜 시간 맥라렌과 함께 재건을 이끌어온 드라이버입니다. "
                    "완벽한 페이스 조절과 휠-투-휠 배틀에서의 정교함이 강점이며, 2026년 시즌 메인 챔피언십 컨텐더로서 입지를 더욱 단단히 다지고 있습니다."
                ),
            },
            {
                "name": "오스카 피아스트리 (Oscar Piastri)",
                "number": "81",
                "nationality": "호주 🇦🇺",
                "short_desc": "냉철한 판단력과 흔들림 없는 침착함을 지닌 챔피언 재목",
                "long_desc": (
                    "오스카 피아스트리는 F3와 F2를 데뷔 첫해에 연속 패권하며 올라온 괴물 같은 재능의 소유자입니다. "
                    "어떠한 압박 상황 속에서도 라디오 통화에서 침착함을 유지하는 일명 'Ice Man' 스타일로, 선배 노리스와 함께 최강의 드라이버 라인업을 형성합니다."
                ),
            },
        ],
    },
    "Aston Martin": {
        "engine": "Honda",
        "base": "Silverstone, United Kingdom",
        "description": "2026년부터 일본의 혼다(Honda) 파워유닛을 독점 공급받아 완전한 워크스 팀(Works Team)으로 거듭난 애스턴 마틴입니다. 실버스톤의 최첨단 풍동 실험실을 발판 삼아 우승을 겨냥합니다.",
        "drivers": [
            {
                "name": "페르난도 알론소 (Fernando Alonso)",
                "number": "14",
                "nationality": "스페인 🇪🇸",
                "short_desc": "베테랑의 관록과 변함없는 스피드를 보여주는 2회 월드 챔피언",
                "long_desc": (
                    "페르난도 알론소는 F1 역사상 가장 많은 레이스 스타트 기록을 가진 철인입니다. "
                    "경기 전체의 레이스 플랜을 머릿속으로 계산하는 '레이스 IQ'가 탁월하며, 40대의 나이에도 여전히 최고 수준의 스피드와 변칙적인 수비 기술을 보여줍니다."
                ),
            },
            {
                "name": "랜스 스트롤 (Lance Stroll)",
                "number": "18",
                "nationality": "캐나다 🇨🇦",
                "short_desc": "빗길 레이스에서 강점을 나타내는 드라이버",
                "long_desc": (
                    "랜스 스트롤은 노면 마찰력이 극도로 낮아지는 웻 노면이나 변칙 기상 조건에서 번뜩이는 레이스 스타트와 스피드를 선보입니다. "
                    "새롭게 변화된 2026 차체 구조에 맞춰 과감한 어택을 시도하고 있습니다."
                ),
            },
        ],
    },
    "Alpine": {
        "engine": "Mercedes",
        "base": "Enstone, United Kingdom",
        "description": "프랑스 알핀 브랜드로, 2026 파워유닛 변화에 발맞추어 고성능 인프라를 적극 수용하고 기술 구조 개편을 단행한 팀입니다.",
        "drivers": [
            {
                "name": "피에르 개슬리 (Pierre Gasly)",
                "number": "10",
                "nationality": "프랑스 🇫🇷",
                "short_desc": "그랑프리 우승 경험을 보유한 정교한 유로파 테크니션",
                "long_desc": (
                    "피에르 개슬리는 몬 자에서 깜짝 우승을 차지했던 경험이 있는 베테랑 드라이버입니다. "
                    "중위권 혼전 속에서 차량의 세팅을 정확히 잡아내는 스티어링 기술과 매끄러운 타이어 관리가 시그니처입니다."
                ),
            },
            {
                "name": "프랑코 콜라핀토 (Franco Colapinto)",
                "number": "43",
                "nationality": "아르헨티나 🇦🇷",
                "short_desc": "남미의 뜨거운 열정과 패기로 무장한 기대주",
                "long_desc": (
                    "프랑코 콜라핀토는 데뷔 직후 공격적인 코너 진입과 주저함 없는 추월 시도로 모터스포츠 팬들의 눈도장을 찍은 드라이버입니다. "
                    "팀의 상위권 진입을 위해 매 레이스 한계까지 차량을 밀어붙입니다."
                ),
            },
        ],
    },
    "Williams": {
        "engine": "Mercedes",
        "base": "Grove, United Kingdom",
        "description": "F1의 역사적인 레전드 명문 윌리엄스입니다. 제임스 바울스 감독의 지휘 아래 최신 설비를 대대적으로 확충하며 명가 부활을 만들어가고 있습니다.",
        "drivers": [
            {
                "name": "알렉산더 알본 (Alex Albon)",
                "number": "23",
                "nationality": "태국 🇹🇭",
                "short_desc": "윌리엄스 재건의 중심축이자 타이어 마술사",
                "long_desc": (
                    "알렉스 알본은 하드 타이어 하나로 극단적인 롱 스틴트를 소화해 내며 포인트를 따내는 뛰어난 경기 운영 능력을 보여줍니다. "
                    "차량의 피드백 전달 능력이 탁월하여 윌리엄스 차량 개선에 일등공신 역할을 담당했습니다."
                ),
            },
            {
                "name": "카를로스 사인츠 (Carlos Sainz)",
                "number": "55",
                "nationality": "스페인 🇪🇸",
                "short_desc": "명석한 두뇌와 뛰어난 안정성을 갖춘 그랑프리 위너",
                "long_desc": (
                    "카를로스 사인츠는 레이스 도중 피트월 엔지니어보다 빠른 전략을 제시하는 지능형 드라이버입니다. "
                    "페라리에서의 우승 경험을 바탕으로 윌리엄스에 승리 DNA를 이식하고 있습니다."
                ),
            },
        ],
    },
    "Racing Bulls": {
        "engine": "Red Bull Ford Powertrains",
        "base": "Faenza, Italy",
        "description": "레드불 그룹의 시스터 팀으로 파엔차 베이스의 젊고 역동적인 레이싱 팀입니다. 신예 육성과 함께 중위권 선두 경쟁을 이끌고 있습니다.",
        "drivers": [
            {
                "name": "리암 로슨 (Liam Lawson)",
                "number": "30",
                "nationality": "뉴질랜드 🇳🇿",
                "short_desc": "대체 출전에서도 강력한 임팩트를 남긴 오세아니아의 신성",
                "long_desc": (
                    "리암 로슨은 과거 갑작스러운 대타 출전 레이스에서도 곧바로 포인트 획득에 성공하며 실력을 검증받은 드라이버입니다. "
                    "상대방과의 치열한 사이드-바이-사이드 배틀에서 물러서지 않는 강인한 배짱을 지녔습니다."
                ),
            },
            {
                "name": "아르비드 린드블라드 (Arvid Lindblad)",
                "number": "41",
                "nationality": "영국 🇬🇧",
                "short_desc": "레드불 주니어 출신의 2026 초신성 루키",
                "long_desc": (
                    "아르비드 린드블라드는 F3에서 단숨에 주목받고 올라온 하이스트 퍼포먼스 유망주입니다. "
                    "2026년 새로운 규정 차량에 빠르게 적응하며 순수한 스피드를 보여주고 있습니다."
                ),
            },
        ],
    },
    "Haas F1 Team": {
        "engine": "Ferrari",
        "base": "Kannapolis, United States",
        "description": "미국 기반의 하스 F1 팀입니다. 페라리와의 견고한 기술 협력 및 도요타 가주 레이싱(TGR)과의 신규 파트너십을 더해 더욱 공격적인 행보를 보여줍니다.",
        "drivers": [
            {
                "name": "에스테반 오콘 (Esteban Ocon)",
                "number": "31",
                "nationality": "프랑스 🇫🇷",
                "short_desc": "강한 디펜스와 끈질긴 레이스로 승부하는 그랑프리 우승자",
                "long_desc": (
                    "에스테반 오콘은 뒤에서 따라오는 추격 차량을 철벽처럼 막아내는 방어 주행에 매우 능합니다. "
                    "어려운 환경 속에서도 끝까지 집요하게 포인트를 챙겨오는 집념이 돋보입니다."
                ),
            },
            {
                "name": "올리버 베어먼 (Oliver Bearman)",
                "number": "87",
                "nationality": "영국 🇬🇧",
                "short_desc": "대체 레이스 데뷔전부터 포인트를 획득한 영국의 차세대 스타",
                "long_desc": (
                    "올리버 베어먼은 준비 없이 투입된 데뷔전 레이스에서도 연신 침착하게 포인트를 따내며 모터스포츠계를 놀라게 했던 신예입니다. "
                    "하스의 2026 프로젝트를 이끌 중요한 기둥입니다."
                ),
            },
        ],
    },
    "Audi": {
        "engine": "Audi",
        "base": "Hinwil, Switzerland",
        "description": "독일의 거대 자동차 제조사 아우디가 자우버(Sauber) 팀을 전격 인수하여 2026년부터 워크스 팀으로 정식 출전합니다. 독일 노이부르크에서 직접 제조한 2026 전용 파워유닛을 탑재합니다.",
        "drivers": [
            {
                "name": "니코 휠켄베르크 (Nico Hülkenberg)",
                "number": "27",
                "nationality": "독일 🇩🇪",
                "short_desc": "아우디 팩토리 프로젝트를 지탱하는 베테랑 테스터 겸 드라이버",
                "long_desc": (
                    "니코 휠켄베르크는 퀄리파잉 한 바퀴에서 차의 한계 이상의 성적을 내는 '베테랑 마법사'입니다. "
                    "아우디 초기 파워유닛 개발과 섀시 밸런스를 구성하는 데 핵심적인 피드백을 제공하고 있습니다."
                ),
            },
            {
                "name": "가브리에우 보르툴레투 (Gabriel Bortoleto)",
                "number": "5",
                "nationality": "브라질 🇧🇷",
                "short_desc": "F3 & F2를 연속 제패하고 상륙한 브라질의 테크니션",
                "long_desc": (
                    "가브리에우 보르툴레투는 브라질 레이싱의 계보를 잇는 특급 신예입니다. "
                    "하위 카테고리 연속 챔피언 출신다운 타이어 관리 능력과 똑부러진 레이스 조율 능력을 갖추고 있습니다."
                ),
            },
        ],
    },
    "Cadillac F1 Team": {
        "engine": "Ferrari",
        "base": "Fishers, United States",
        "description": "2026년 그리드에 합류한 11번째 신생 팀 GM 제너럴 모터스의 캐딜락 F1 팀입니다. 페라리 파워유닛을 바탕으로 미국 자본의 막강한 기술력을 F1 그리드에 펼쳐 보입니다.",
        "drivers": [
            {
                "name": "세르히오 페레스 (Sergio Pérez)",
                "number": "11",
                "nationality": "멕시코 🇲🇽",
                "short_desc": "타이어 세이빙과 추월쇼의 대명사 '체코'",
                "long_desc": (
                    "세르히오 페레스는 장거리 레이스에서 타이어 수명을 극단적으로 늘리는 주행 테크닉이 전매특허입니다. "
                    "신생 캐딜락 팀의 초기 세팅을 안정화하고 중위권 상위 포인트를 목표로 달립니다."
                ),
            },
            {
                "name": "발테리 보타스 (Valtteri Bottas)",
                "number": "77",
                "nationality": "핀란드 🇫🇮",
                "short_desc": "10회 이상 그랑프리 우승에 빛나는 베테랑의 정석",
                "long_desc": (
                    "발테리 보타스는 메르세데스 시절 10회 이상의 우승과 무수한 폴 포지션을 기록했던 검증된 원톱급 드라이버입니다. "
                    "캐딜락 F1 팀이 그리드에 신속히 안착하는 데 있어 결정적인 데이터와 스피드를 제공합니다."
                ),
            },
        ],
    },
}

schedule_data = [
    {
        "Round": 1,
        "Grand Prix": "호주 그랑프리",
        "Location": "🇦🇺 멜버른 (알버트 파크 서킷)",
        "Date": "2026-03-08",
    },
    {
        "Round": 2,
        "Grand Prix": "중국 그랑프리",
        "Location": "🇨🇳 상하이 (상하이 인터내셔널 서킷)",
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
        "Location": "🇺🇸 미국 마이애미 (마이애미 인터내셔널 오토드롬)",
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
        "Location": "🇪🇸 바르셀로나 (서킷 드 바르셀로나-카탈루냐)",
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
        "Location": "🇧🇪 스파 (서킷 드 스파-프랑코샹)",
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
        "Location": "🇳🇱 잔트보르트 (서킷 잔트보르트)",
        "Date": "2026-08-23",
    },
    {
        "Round": 13,
        "Grand Prix": "이탈리아 그랑프리",
        "Location": "🇮🇹 몬자 (아우토드로모 나치오날레 몬자)",
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
        "Location": "🇸🇬 싱가포르 (마리나 베이 스트리트 서킷)",
        "Date": "2026-10-04",
    },
    {
        "Round": 16,
        "Grand Prix": "미국 그랑프리",
        "Location": "🇺🇸 오스틴 (서킷 오브 디 아메리카스)",
        "Date": "2026-10-18",
    },
    {
        "Round": 17,
        "Grand Prix": "멕시코 그랑프리",
        "Location": "🇲🇽 멕시코시티 (아우토드로모 에르마노스 로드리게스)",
        "Date": "2026-10-25",
    },
    {
        "Round": 18,
        "Grand Prix": "상파울루 그랑프리",
        "Location": "🇧🇷 상파울루 (아우토드로모 호세 카를로스 파체)",
        "Date": "2026-11-08",
    },
    {
        "Round": 19,
        "Grand Prix": "라스베이거스 그랑프리",
        "Location": "🇺🇸 라스베이거스 (라스베이거스 스트리트 서킷)",
        "Date": "2026-11-21",
    },
    {
        "Round": 20,
        "Grand Prix": "카타르 그랑프리",
        "Location": "🇶🇦 루사일 (루사일 인터내셔널 서킷)",
        "Date": "2026-11-29",
    },
    {
        "Round": 21,
        "Grand Prix": "아부다비 그랑프리",
        "Location": "🇦🇪 아부다비 (야스 마리나 서킷)",
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

    # 입력값이 있을 때 매칭 검색 진행
    matched_teams = []

    if search_input:
        query_lower = search_input.lower()
        for official_name, aliases in team_aliases.items():
            # 키워드 매칭 여부 검사
            if any(query_lower in alias.lower() for alias in aliases) or (
                query_lower in official_name.lower()
            ):
                matched_teams.append(official_name)

    # 검색을 진행하지 않았을 때
    if not search_input:
        st.info(
            "💡 검색창에 팀명을 입력해 주세요. (입력 시 해당 팀의 세부 정보와 드라이버 라인업이 펼쳐집니다)"
        )

    # 검색 결과가 없을 때
    elif search_input and not matched_teams:
        st.error(f"'{search_input}' 에 대한 검색 결과가 없습니다.")

    # 검색 결과 출력
    else:
        for team_name in matched_teams:
            info = teams_data[team_name]

            # 팀 카드 UI
            st.markdown(
                f"""
                <div class="f1-card">
                    <h2 style="color: #ffffff !important; margin-bottom: 10px;">🏎️ {team_name}</h2>
                    <p style="font-size: 1.05rem;"><b>⚙️ 파워 유닛:</b> <span style="color: #e10600 !important;">{info['engine']}</span></p>
                    <p style="font-size: 1.05rem;"><b>📍 팀 베이스:</b> {info['base']}</p>
                    <hr style="border-color: #333344; margin: 15px 0;">
                    <p style="font-size: 1.0rem; line-height: 1.6; color: #dddddd !important;">{info['description']}</p>
                </div>
                """,
                unsafe_allow_html=True,
            )

            st.markdown("### 🏎️ 2026 드라이버 라인업")
            st.markdown(
                "<p style='color: #aaaaaa !important;'>드라이버를 클릭하면 상세 프로필과 커리어 설명을 보실 수 있습니다.</p>",
                unsafe_allow_html=True,
            )

            for driver in info["drivers"]:
                # 드라이버 클릭 방식 (Expander 적용)
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
# Page 2: Grand Prix Schedule
# ---------------------------------------------------------
else:
    st.subheader("📅 2026 F1 그랑프리 일정표")

    today = datetime.now().date()
    formatted_schedule = []

    for race in schedule_data:
        race_date = datetime.strptime(race["Date"], "%Y-%m-%d").date()
        is_completed = race_date < today

        formatted_schedule.append(
            {
                "라운드": f"Round {race['Round']}",
                "그랑프리": race["Grand Prix"],
                "개최 국가 및 서킷": race["Location"],
                "레이스 일자": race["Date"],
                "진행 상태": "✅ 종료됨" if is_completed else "🏁 예정됨",
            }
        )

    df = pd.DataFrame(formatted_schedule)

    completed_count = sum(1 for r in formatted_schedule if "종료됨" in r["진행 상태"])
    total_count = len(schedule_data)

    m1, m2, m3 = st.columns(3)
    m1.metric("총 라운드 수", f"{total_count} GP")
    m2.metric("진행 완료", f"{completed_count} GP")
    m3.metric("남은 경기", f"{total_count - completed_count} GP")

    st.divider()

    # 진행 상태 색상 강조
    def highlight_completed(val):
        if "종료됨" in str(val):
            return "color: #4CAF50; font-weight: bold;"
        return "color: #FF9800; font-weight: bold;"

    st.dataframe(
        df.style.applymap(highlight_completed, subset=["진행 상태"]),
        use_container_width=True,
        height=600,
    )
