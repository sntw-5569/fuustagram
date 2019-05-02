<template>
  <main class="main-contents">
    <div id="article-container" class="section is-center content-area">
        <article-panel v-for="(article, index) in articleData" :key="index"
          :modalControl="modalControl" :contents="article" />
    </div>
    <div div id="pict-modal" class="modal" v-bind:class="{'is-active': isModal}">
        <div class="modal-background" @click="modalControl(null, false)"></div>
        <div class="modal-content">
          <p class="image">
            <img :src="selectImage" alt="">
          </p>
        </div>
        <button class="modal-close is-large" aria-label="close"
         @click="modalControl(null, false)"></button>
      </div>
  </main>
</template>

<script>
import ArticlePanel from "./article/ArticlePanel"

export default {
  name: "main-contents",
  props: [
    "articleData"
  ],
  components:{
    ArticlePanel
  },
  data() {
    return {
      errorMessage: "",
      isFilterd: false,
      selectImage: null,
      isModal: false
    }
  },
  methods: {
    modalControl: function(img, isShow) {
      this.selectImage = img
      this.isModal = isShow
      if(isShow) {
        document.querySelector('html').classList.add('is-clipped')
      } else {
        document.querySelector('html').classList.remove('is-clipped')
      }
    }
  }
}
</script>

<style lang="scss" scoped>
.main-contents {
  padding: 10px 0; 
  background-color: rgb(240, 248, 239);
}
.modal {
  z-index: 100;
}
@media screen and (min-width : 300px){
    .content-area {
    padding: 0 10%;
  }
}
@media screen and (min-width : 720px){
  .content-area {
    padding: 0 20%;
    margin-bottom: 50px;
  }
}
@media screen and (min-width : 1600px){
  .content-area {
    padding: 0 30%;
    margin-bottom: 50px;
  }
}
</style>
