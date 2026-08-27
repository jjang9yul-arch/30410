import streamlit as st

st.set_page_config(
    page_title="F1 2026 시즌 공식 백과사전",
    page_icon="🏎️",
    layout="wide"
)

# Custom CSS - 대형 F1 로고 및 전체 칸 활용, 하얀 글씨, 상세 서사 레이아웃
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@600;800;900&family=Noto+Sans+KR:wght@400;700;900&display=swap');

    .stApp {
        background: linear-gradient(135deg, #07090f 0%, #11151f 50%, #030406 100%);
        color: #ffffff !important;
        font-family: 'Noto Sans KR', sans-serif;
    }

    /* 상단 F1 로고 영역 (다시 크게 복원) */
    .f1-header-container {
        display: flex;
        justify-content: center;
        align-items: center;
        padding: 20px 0;
        border-bottom: 3px solid rgba(225, 6, 0, 0.8);
        margin-bottom: 30px;
        background: rgba(0, 0, 0, 0.3);
    }

    .f1-logo-img {
        width: 100%;
        max-width: 600px; /* 로고 크기를 다시 큼직하게 확장 */
        height: auto;
        object-fit: contain;
        filter: drop-shadow(0px 0px 25px rgba(225, 6, 0, 0.9));
    }

    /* 하얀 글씨 보장 */
    h1, h2, h3, h4, h5, h6, p, span, label, div {
        color: #ffffff !important;
    }

    /* 팀 카드 디자인 */
    .team-card {
        background: rgba(18, 23, 33, 0.9);
        border-radius: 14px;
        border: 1px solid rgba(255, 255, 255, 0.15);
        padding: 25px;
        margin-bottom: 25px;
        box-shadow: 0 8px 25px rgba(0, 0, 0, 0.5);
    }

    .team-title {
        font-family: 'Orbitron', sans-serif;
        font-size: 1.8rem;
        font-weight: 900;
        letter-spacing: 1px;
    }

    .stat-badge {
        display: inline-block;
        background: rgba(225, 6, 0, 0.25);
        border: 1px solid rgba(225, 6, 0, 0.6);
        color: #ff6b6b !important;
        padding: 5px 14px;
        border-radius: 20px;
        font-size: 0.9rem;
        font-weight: 700;
        margin-right: 10px;
        margin-top: 10px;
    }

    /* 드라이버 서사형 상세 프로필 카드 */
    .driver-story-card {
        background: #111622;
        border-radius: 12px;
        border: 1px solid #2a3447;
        padding: 20px;
        margin-bottom: 20px;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.4);
    }

    .driver-num {
        font-family: 'Orbitron', sans-serif;
        color: #e10600 !important;
        font-size: 1.4rem;
        font-weight: 900;
    }

    .driver-name {
        font-size: 1.25rem;
        font-weight: 800;
        color: #ffffff !important;
        margin: 4px 0;
    }

    .driver-story-text {
        font-size: 0.95rem;
        color: #d1d5db !important;
        line-height: 1.6;
        margin-top: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# 1. 상단 대형 F1 로고 헤더
st.markdown("""
    <div class="f1-header-container">
        <img class="f1-logo-img" src="https://upload.wikimedia.org/wikipedia/commons/3/33/F1.svg" alt="F1 Logo">
    </div>
""", unsafe_allow_html=True)

# 2026 시즌 전체 11개 팀 및 서사가 담긴 드라이버 상세 데이터베이스 (22명 전체)
f1_teams_database = [
    {
        "team_en": "Mercedes-AMG Petronas F1 Team", "team_kr": "메르세데스", "color": "#27F4D2", "principal": "Toto Wolff", "power_unit": "Mercedes",
        "team_desc": "2026년 대대적인 규정 변화 속에서 파워유닛 명가의 저력을 유감없이 발휘하며 챔피언십 선두를 질주하고 있는 최강의 워크스 팀입니다.",
        "drivers": [
            {
                "name_en": "Kimi Antonelli", "name_kr": "키미 안토넬리", "number": "12", "country": "이탈리아 🇮🇹", "birth": "2006.08.25",
                "story": "주니어 포뮬러 시절부터 압도적인 재능으로 모터스포츠계를 뒤흔들며 '넥스트 베르스타펜'으로 지목받았습니다. 메르세데스의 전폭적인 지지 속에 메인 시트에 데뷔하자마자 시즌 초반부터 경이로운 기속력과 침착함을 선보이며 수차례 우승을 거머쥐고 팀의 핵심 에이스로 완전히 자리 잡았습니다."
            },
            {
                "name_en": "George Russell", "name_kr": "조지 러셀", "number": "63", "country": "영국 🇬🇧", "birth": "1998.02.15",
                "story": "윌리엄스 시절부터 '미스터 토요일'이라 불릴 만큼 극단적인 예선 집중력과 타협 없는 주행을 보여줬습니다. 메르세데스 이적 후 팀의 리더로서 날카로운 데이터 분석력과 냉철한 판단력을 무장해 매 경기 안정적인 포디움 피니시를 달성하며 은빛 화살의 황금기를 이끌고 있습니다."
            }
        ]
    },
    {
        "team_en": "Scuderia Ferrari", "team_kr": "페라리", "color": "#E8002d", "principal": "Frédéric Vasseur", "power_unit": "Ferrari",
        "team_desc": "티포시들의 뜨거운 열정과 함께 F1 역사상 전무후무한 최다 우승 기록을 향해 질주하는 이탈리아의 자존심입니다.",
        "drivers": [
            {
                "name_en": "Lewis Hamilton", "name_kr": "루이스 해밀턴", "number": "44", "country": "영국 🇬🇧", "birth": "1985.01.07",
                "story": "통산 7회 월드 챔피언에 빛나는 F1 역사상 가장 위대한 살아있는 전설입니다. 커리어의 황혼기에서 페라리로 이적이라는 대담한 도전을 감행했으며, 스칼렛 레드 머신을 타고 전 세계 티포시들의 염원인 통산 8번째 월드 타이틀을 들어 올리기 위해 목숨을 건 레이스를 펼치고 있습니다."
            },
            {
                "name_en": "Charles Leclerc", "name_kr": "샤를 르클레르", "number": "16", "country": "모나코 🇲🇨", "birth": "1997.10.16",
                "story": "페라리 아카데미가 배출한 역대급 원랩 스페셜리스트이자 모나코의 영웅입니다. 홈 그랑프리의 저주를 극복하고 우승을 차지했던 순간처럼, 한계 상황에서도 코너링의 극한을 이끌어내는 공격적인 드라이빙 스타일로 페라리의 오랜 우승 갈증을 해소하고자 온 힘을 쏟고 있습니다."
            }
        ]
    },
    {
        "team_en": "McLaren Formula 1 Team", "team_kr": "맥라렌", "color": "#FF8000", "principal": "Andrea Stella", "power_unit": "Mercedes",
        "team_desc": "끊임없는 기술 혁신과 눈부신 에어로다이내믹 샤시 업그레이드로 최상위권 판도를 주도하는 전통의 명문 팀입니다.",
        "drivers": [
            {
                "name_en": "Lando Norris", "name_kr": "랜도 노리스", "number": "4", "country": "영국 🇬🇧", "birth": "1999.11.13",
                "id": "lannor",
                "story": "재치 있는 성격 뒤에 숨겨진 서킷 위의 폭발적인 투지와 천재적인 감각의 소유자입니다. 맥라렌의 암흑기를 함께 견뎌낸 뒤 팀의 급격한 성장에 발맞춰 매 시즌 우승 트로피를 사냥하며 명가 재건을 완수하고 있는 맥라렌의 명실상부한 메인 에이스입니다."
            },
            {
                "name_en": "Oscar Piastri", "name_kr": "오스카 피아스트리", "number": "81", "country": "호주 🇦🇺", "birth": "2001.04.06",
                "story": "주니어 카테고리 전 시리즈를 루키 시즌에 제패한 뒤 F1에 입성한 '포커페이스의 천재'입니다. 치열한 접전 중에도 신입답지 않은 서늘한 침착성과 완벽한 타이어 매니지먼트를 선보이며 베테랑들을 압박하는 차세대 챔피언 후보로 꼽힙니다."
            }
        ]
    },
    {
        "team_en": "Oracle Red Bull Racing", "team_kr": "레드불 레이싱", "color": "#3671C6", "principal": "Christian Horner", "power_unit": "Red Bull Ford",
        "team_desc": "포드와의 독창적인 자체 파워유닛 파트너십을 구축하며 새로운 모터스포츠의 장을 열어가고 있는 강호 팀입니다.",
        "drivers": [
            {
                "name_en": "Max Verstappen", "name_kr": "막스 베르스타펜", "number": "1", "country": "네덜란드 🇳🇱", "birth": "1997.09.30",
                "story": "타협 없는 공격성과 한 치의 오차도 용납하지 않는 정교한 주행 능력으로 F1의 패러다임을 바꾼 괴물 같은 챔피언입니다. 차량 성능의 열세 속에서도 기발한 레이스 운영과 경이로운 집중력으로 매 경기 기적 같은 포인트를 짜내며 자신의 지배력을 증명하고 있습니다."
            },
            {
                "name_en": "Isack Hadjar", "name_kr": "아이작 하자르", "number": "6", "country": "프랑스 🇫🇷", "birth": "2004.09.28",
                "story": "레드불 주니어 프로그램의 거친 검증 과정을 모두 통과해 정식 시트를 꿰찬 투지 넘치는 프랑스 신예입니다. 거침없는 패기와 폭발적인 코너 탈출 속도를 무기로 세계 최고의 드라이버들과 어깨를 나란히 하며 새로운 도약을 준비하고 있습니다."
            }
        ]
    },
    {
        "team_en": "Visa Cash App Racing Bulls", "team_kr": "레이싱 불스 (RB)", "color": "#6692FF", "principal": "Laurent Mekies", "power_unit": "Red Bull Ford",
        "team_desc": "젊은 피의 혈기와 패기를 바탕으로 중위권 판도를 뒤흔드는 레드불 패밀리의 핵심 영건 육성 팀입니다.",
        "drivers": [
            {
                "name_en": "Liam Lawson", "name_kr": "리암 로슨", "number": "30", "country": "뉴질랜드 🇳🇿", "birth": "2002.02.11",
                "story": "대타 출전 기회를 실력으로 완벽하게 증명해 내며 정식 시트를 거머쥔 뉴질랜드 출신의 파이터입니다. 불굴의 투지와 몸을 사리지 않는 과감한 추월 능력을 지니고 있어, 매 주말 까다로운 중위권 싸움에서 팀에 값진 승점를 안겨주는 핵심 전력입니다."
            },
            {
                "name_en": "Arvid Lindblad", "name_kr": "아르비드 린드블라드", "number": "41", "country": "영국 🇬🇧", "birth": "2007.08.08",
                "story": "카트부터 하위 포뮬러까지 눈부신 스피드로 파란을 일으키며 초고속으로 F1 무대에 승선한 특급 루키입니다. 나이가 믿기지 않는 대담한 레이스 운영과 영리한 경기 조율 능력을 보여주며 모터스포츠 팬들의 기대를 한몸에 받고 있습니다."
            }
        ]
    },
    {
        "team_en": "BWT Alpine F1 Team", "team_kr": "알핀", "color": "#FF87BC", "principal": "Oliver Oakes", "power_unit": "Mercedes",
        "team_desc": "프랑스 자동차의 자존심을 걸고 차량의 한계를 돌파하며 상위권 도약을 노리는 워크스 팀입니다.",
        "drivers": [
            {
                "name_en": "Pierre Gasly", "name_kr": "피에르 개슬리", "number": "10", "country": "프랑스 🇫🇷", "birth": "1996.02.07",
                "story": "수많은 시련과 역경을 딛고 일어선 불굴의 레이서이자 눈물겨운 우승 경험을 지닌 베테랑입니다. 다소 아쉬운 성능의 머신을 타고도 매번 드라이버의 역량을 120% 이끌어내는 신들린 레이스 크래프트로 알핀의 든든한 정신적 지주 역할을 해내고 있습니다."
            },
            {
                "name_en": "Franco Colapinto", "name_kr": "프랑코 콜라핀토", "number": "43", "country": "아르헨티나 🇦🇷", "birth": "2003.05.27",
                "story": "남미 팬들의 열광적인 지지를 업고 F1 무대에 센세이션을 일으키며 합류한 아르헨티나의 스타입니다. 데뷔 초기부터 거침없는 주행 감각과 뛰어난 피드백 능력을 발휘하며 팀에 활력을 불어넣고 있는 매력적인 젊은 드라이버입니다."
            }
        ]
    },
    {
        "team_en": "TGR Haas F1 Team", "team_kr": "하스", "color": "#B6BABD", "principal": "Ayao Komatsu", "power_unit": "Ferrari",
        "team_desc": "미국 아메리칸 스피드의 감성과 효율적인 예산 운영을 결합해 실속 있는 중위권 레이스를 펼치는 팀입니다.",
        "drivers": [
            {
                "name_en": "Esteban Ocon", "name_kr": "에스테반 오콘", "number": "31", "country": "프랑스 🇫🇷", "birth": "1996.09.17",
                "story": "철저한 타이어 관리와 한 치의 실 수도 용납하지 않는 정교한 방어 주행이 특기인 베테랑 프랑스 드라이버입니다. 까다로운 트랙 상황에서도 집중력을 잃지 않고 점수를 긁어모으는 특유의 레이싱 지능으로 하스의 중위권 순위 싸움을 진두지휘하고 있습니다."
            },
            {
                "name_en": "Oliver Bearman", "name_kr": "올리버 베어먼", "number": "87", "country": "영국 🇬🇧", "birth": "2005.05.08",
                "story": "페라리 비상 대타 출전 당시 전 세계를 경악게 했던 천재적인 주행 실력을 바탕으로 풀타임 시트를 쟁취했습니다. 젊은 나이에도 불구하고 침착한 경기 흐름 파악과 과감한 승부수를 던질 줄 아는 대담함을 겸비해 차세대 스타로 급부상 중입니다."
            }
        ]
    },
    {
        "team_en": "Audi F1 Team", "team_kr": "아우디 (자우버)", "color": "#00E785", "principal": "Mattia Binotto", "power_unit": "Audi",
        "team_desc": "전통의 자우버 팀을 인수하여 독일의 프리미엄 자동차 명가 아우디가 전격적으로 뛰어든 야심 찬 워크스 프로젝트입니다.",
        "drivers": [
            {
                "name_en": "Nico Hülkenberg", "name_kr": "니코 휠켄베르크", "number": "27", "country": "독일 🇩🇪", "birth": "1987.08.19",
                "story": "F1에서 가장 정교하고 날카로운 예선 한 방 능력을 지닌 것으로 평가받는 독일 모터스포츠의 상징입니다. 풍부한 테크니컬 피드백 능력을 인정받아 아우디 프로젝트의 첫 초석을 다지는 중차대한 임무를 맡아 팀을 이끌고 있습니다."
            },
            {
                "name_en": "Gabriel Bortoleto", "name_kr": "가브리에우 보르툴레투", "number": "5", "country": "브라질 🇧🇷", "birth": "2004.10.14",
                "story": "하위 포뮬러 무대를 차근차근 제패하며 실력을 입증한 뒤 아우디의 미래를 책임질 메인 시트에 낙점된 브라질의 신예입니다. 영리하고 안정적인 포인트 피니시 능력이 강점이며, 전설들의 뒤를 잇는 브라질 레이싱의 희망으로 기대를 모읍니다."
            }
        ]
    },
    {
        "team_en": "Atlassian Williams Racing", "team_kr": "윌리엄스", "color": "#64C4FF", "principal": "James Vowles", "power_unit": "Mercedes",
        "team_desc": "찬란했던 역사를 뒤로하고 대대적인 체질 개선과 기술 혁신을 통해 명가 부활의 기적을 써 내려가는 전통의 팀입니다.",
        "drivers": [
            {
                "name_en": "Carlos Sainz", "name_kr": "카를로스 사인츠", "number": "55", "country": "스페인 🇪🇸", "birth": "1994.09.01",
                "story": "'레이스 교수'라는 별명에 걸맞게 뛰어난 전략 분석력과 엔지니어링 이해도를 지닌 완성형 드라이버입니다. 페라리에서 거둔 눈부신 성공을 뒤로하고 윌리엄스로 이적해, 팀 전체의 체질을 바꾸고 중상위권 도약을 이뤄내는 핵심 구원투수로 활약 중입니다."
            },
            {
                "name_en": "Alexander Albon", "name_kr": "알렉산더 알본", "number": "23", "country": "태국 🇹🇭", "birth": "1996.03.23", "story": "어려운 환경의 머신을 타고도 매번 마법 같은 주행으로 포인트를 건져 올려 '윌리엄스의 구세주'라 불립니다. 탁월한 타이어 세이브 능력과 온화한 성품 속 숨겨진 날카로운 승부욕으로 팀원들의 신뢰를 한몸에 받는 리드 드라이버입니다."
            }
        ]
    },
    {
        "team_en": "Aston Martin Aramco F1 Team", "team_kr": "애스턴 마틴", "color": "#229971", "principal": "Andy Cowell", "power_unit": "Honda",
        "team_desc": "최첨단 팩토리 인프라와 혼다 파워유닛의 결합을 통해 챔피언십 정상을 조준하는 브리티시 럭셔리 워크스 팀입니다.",
        "drivers": [
            {
                "name_en": "Fernando Alonso", "name_kr": "페르난도 알론소", "number": "14", "country": "스페인 🇪🇸", "birth": "1981.07.29",
                "story": "나이를 거꾸로 먹는 듯한 경이로운 반사 신경과 서킷 전체를 조망하는 맹수 같은 시야를 지닌 불멸의 전설입니다. 수십 년의 커리어 동안 쌓아온 모든 노하우를 동원해 애스턴 마틴이 최상위권으로 도약하는 발판을 홀로 단단히 지탱하고 있습니다."
            },
            {
                "name_en": "Lance Stroll", "name_kr": "랜스 스트롤", "number": "18", "country": "캐나다 🇨🇦", "birth": "1998.10.29",
                "story": "비가 내리는 악천후 서킷이나 예측 불가능한 혼전 상황에서 유독 빛을 발하는 폭발적인 집중력의 소유자입니다. 팀의 오랜 프로젝트와 함께하며 수많은 경험을 축적했고, 결정적인 순간마다 예리한 추월을 성공시키며 팀의 저력을 과시합니다."
            }
        ]
    },
    {
        "team_en": "Cadillac F1 Team", "team_kr": "캐딜락 F1 팀", "color": "#FFD700", "principal": "Graeme Lowdon", "power_unit": "Ferrari",
        "team_desc": "미국 제너럴 모터스(GM)의 막강한 자본력과 기술력을 바탕으로 2026년 F1 무대에 새롭게 지각변동을 일으키는 창단 팀입니다.",
        "drivers": [
            {
                "name_en": "Valtteri Bottas", "name_kr": "발테리 보타스", "number": "77", "country": "핀란드 🇫🇮", "birth": "1989.08.28",
                "story": "통산 10회 우승을 기록하며 메르세데스의 전성기를 이끌었던 베테랑 중의 베테랑입니다. 풍부한 개발 경험과 흔들리지 않는 멘탈을 바탕으로, F1에 첫발을 디딘 신생 캐딜락 팀의 머신 셋업 기준점과 방향성을 제시하는 중대한 임무를 맡고 있습니다."
            },
            {
                "name_en": "Sergio Pérez", "name_kr": "세르히오 페레스", "number": "11", "country": "멕시코 🇲🇽", "birth": "1990.01.26",
                "story": "시가지 서킷의 마법사라 불리며 누구도 따라올 수 없는 환상적인 타이어 관리 능력을 지닌 멕시코의 국민 영웅입니다. 오랜 기간 최정상급 팀에서 갈고닦은 노련한 레이스 운영으로 캐딜락 팀이 빠르게 그리드에 안착하는 데 결정적인 기여를 하고 있습니다."
            }
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

# 탭 메뉴 구성
tab1, tab2, tab3 = st.tabs(["🔍 F1 팀 검색 및 선수 서사", "🏎️ 2026 전체 11개 팀 백과사전", "📅 2026 그랑프리 일정 & 포디움"])

# [탭 1] 팀 검색 및 드라이버 심층 서사
with tab1:
    st.subheader("🔍 F1 팀 및 드라이버 심층 검색")
    st.caption("원하시는 팀을 선택하면 팀의 상세 소개와 각 드라이버의 서사 및 프로필을 깊이 있게 확인하실 수 있습니다.")
    st.write("")
    
    team_name_list = [t["team_kr"] for t in f1_teams_database]
    selected_search_team = st.selectbox("검색할 팀 선택하기", team_name_list)
    
    for team in f1_teams_database:
        if team["team_kr"] == selected_search_team:
            st.markdown(f"""
                <div class="team-card" style="border-top: 6px solid {team['color']};">
                    <div class="team-title" style="color: {team['color']};">{team['team_en']} ({team['team_kr']})</div>
                    <p style="margin: 12px 0 15px 0; font-size: 1.1rem; color: #ffffff;">{team['team_desc']}</p>
                    <div>
                        <span class="stat-badge">팀 디렉터 / 감독: {team['principal']}</span>
                        <span class="stat-badge">파워 유닛: {team['power_unit']}</span>
                    </div>
                </div>
            """, unsafe_allow_html=True)
            
            st.markdown("### 📖 소속 드라이버 심층 서사 및 프로필")
            d_cols = st.columns(2)
            for idx, driver in enumerate(team["drivers"]):
                with d_cols[idx]:
                    st.markdown(f"""
                        <div class="driver-story-card">
                            <div class="driver-num">#{driver['number']}</div>
                            <div class="driver-name">{driver['name_kr']} ({driver['name_en']})</div>
                            <hr style="border-color: rgba(255,255,255,0.1); margin: 10px 0;">
                            <p style="margin: 4px 0; color: #e2e8f0;"><b>국적:</b> {driver['country']}</p>
                            <p style="margin: 4px 0; color: #e2e8f0;"><b>생년월일:</b> {driver['birth']}</p>
                            <div class="driver-story-text"><b>서사 및 커리어:</b><br>{driver['story']}</div>
                        </div>
                    """, unsafe_allow_html=True)

# [탭 2] 2026 전체 11개 팀 백과사전
with tab2:
    st.subheader("🏁 2026 시즌 공식 11개 팀 및 22명 드라이버 총람")
    st.caption("신생 캐딜락 팀을 포함한 모든 2026 그리드 구성원의 상세 서사와 팀 정보입니다.")
    st.write("")

    for team in f1_teams_database:
        st.markdown(f"""
            <div class="team-card" style="border-left: 8px solid {team['color']};">
                <div class="team-title" style="color: {team['color']};">{team['team_en']} ({team['team_kr']})</div>
                <p style="margin: 10px 0; color: #ffffff; font-size: 1.05rem;">{team['team_desc']}</p>
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
                    <div class="driver-story-card">
                        <div class="driver-num">#{driver['number']}</div>
                        <div class="driver-name">{driver['name_kr']} ({driver['name_en']})</div>
                        <p style="margin: 4px 0; font-size: 0.9rem; color: #cbd5e0;">국적: {driver['country']} | 생년월일: {driver['birth']}</p>
                        <div class="driver-story-text" style="font-size: 0.9rem;">{driver['story']}</div>
                    </div>
                """, unsafe_allow_html=True)
        st.write("---")

# [탭 3] 2026 그랑프리 일정표 및 포디움 결과
with tab3:
    st.subheader("📅 2026 FIA F1 월드 챔피언십 전체 일정 & 포디움 결과")
    st.caption("완료된 그랑프리는 우측에 실제 2026 포디움(TOP 3) 결과가 상세하게 연동되어 있습니다.")
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
