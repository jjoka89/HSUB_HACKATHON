// 학과 저장하는 객체
const major = {
  // 학과별 데이터베이스
  engineering: [
    // 계열별로 나누고 그 안에 학과별로 나눔
    { 기계공학과: [] }, // 기계 공학과 게시글 리스트
    { 컴퓨터공학과: [] },
    { 전기_전자공학과: [] },
    { 환경공학과: [] },
    { 건축공학과: [] },
  ],
  business: [
    { 경제학과: [] },
    { 경영학과: [] },
    { 통계학과: [] },
    { 회계학과: [] },
  ],
};
// console.log(major);
console.log(String(Object.keys(major.engineering[0]))); // 학과 이름 찾기

// 임시로 만든 게시글들  (localStorage에 저장할 객체)
const tempPostList = [
  {
    id: 1,
    title: "해커톤 준비하기",
    content: "게시판 만들기 너무 어렵다",
    comment: [
      { text: "자바스크립트", userName: "이현진4" },
      { text: "리액트와 타입스크립트", userName: "이현진3" },
      { text: "html과 css", userName: "이현진2" },
    ],
    commentCount: 0,
    like: Boolean,
    saved: Boolean,
    userName: "이현진",
  },
  {
    id: 2,
    title: "수강신청 날짜 아시는 분?",
    content: "8월 9일부터 11일까지 입니다.",
    comment: [{ text: "이틀 뒤입니다....", userName: "이현진4" }],
    commentCount: 0,
    like: Boolean,
    saved: Boolean,
    userName: "이현진2",
  },
  {
    id: 3,
    title: "다들 개강 언제인가요?",
    content: "전 한달도 안남았어요ㅠㅠ",
    comment: [
      { text: "이틀 뒤입니다....", userName: "이현진3" },
      { text: "우영우 보니까 방학 끝났네", userName: "이현진7" },
    ],
    commentCount: 0,
    like: Boolean,
    saved: Boolean,
    userName: "이현진3",
  },
  {
    id: 2,
    title: "멋쟁이사자 해커톤 2주 남았다",
    content: "abcdefu~~",
    comment: [{ text: "레전드", userName: "이현진2" }],
    commentCount: 0,
    like: Boolean,
    saved: Boolean,
    userName: "이현진4",
  },
  {
    id: 2,
    title: "수강신청 날짜 아시는 분?",
    content: "8월 9일부터 11일까지 입니다.",
    comment: [{ text: "이틀 뒤입니다....", userName: "이현진4" }],
    commentCount: 0,
    like: Boolean,
    saved: Boolean,
    userName: "이현진5",
  },
];

console.log(major["engineering"][0]); // major객체에서 기계공학과 객체에 접근

// major에 게시글목록을 넣어준다
major["engineering"][0].기계공학과 = tempPostList;
console.log(major);

// 객체를 JSON문자열로 변환
const majorListStrings = JSON.stringify(major);

// setItem   (key, value) - localStorage에 저장하기
window.localStorage.setItem("major", majorListStrings);
