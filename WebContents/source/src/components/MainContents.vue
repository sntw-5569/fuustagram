<template>
  <main class="main-contents n-scroll">
    <ul class="n-list">
      <li> <img class="-no-disp" src="../assets/logo.png"> </li>
      <li> <article-panel :imageUrl="imgUrl" /> </li>
      <li> <article-panel :imageUrl="imgUrl" /> </li>
      <li> <article-panel :imageUrl="imgUrl" /> </li>
      <li> <article-panel :imageUrl="imgUrl" /> </li>
      <li> <article-panel :imageUrl="imgUrl" /> </li>
    </ul>
  </main>
</template>

<script>
import ArticlePanel from "./article/ArticlePanel"
// import TempImage from "../assets/under_construction.jpg"
import TempImage from "../assets/logo.png"


export default {
  name: "main-contents",
  components:{
    ArticlePanel
  },
  data() {
    return {
      errorMessage: "",
      isFilterd: false,
      imgUrl: TempImage
    }
  },
  methods: {
  }
}
</script>

<style lang="scss" scoped>
.main-contents {
  padding-top: 50px; 
  padding-bottom: 5px; 
  // background-color: green;
  background-color: snow;
}
.vertical-list {
  li {
    display: block;
  }
}
</style>
