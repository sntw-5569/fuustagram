<template>
  <main class="main-contents">
    <div class="section is-center content-area">
      <!-- temporary data -->
        <article-panel :modalControl="modalControl" :contents="tmpData" />
        <article-panel :modalControl="modalControl" :contents="tmpData" />
        <article-panel :modalControl="modalControl" :contents="tmpData" />
        <article-panel :modalControl="modalControl" :contents="tmpData" />
        <article-panel :modalControl="modalControl" :contents="tmpData" />
      <!-- temporary data -->
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
      imgUrl: TempImage,
      selectImage: null,
      isModal: false,
      tmpData: {
        'text': 'this is detail text.\nsample inner comment.',
        'imageUrl': TempImage,
        'tagList': [
          '#sample1',
          '#sample2',
          '#sample3',
        ]
      }
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
  // background-color: green;
  background-color: rgb(240, 248, 239);
}
@media screen and (min-width : 300px){
    .content-area {
    padding: 0 10%;
  }
}
@media screen and (min-width : 720px){
  .content-area {
    padding: 0 20%;
  }
}
@media screen and (min-width : 1600px){
  .content-area {
    padding: 0 30%;
  }
}
</style>
