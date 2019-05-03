<template>
  <main class="main-contents" oncontextmenu="return false;">
    <div id="article-container" class="section is-center content-area">
        <article-panel v-for="(article, index) in articleData" :key="index"
          :modalControl="modalControl" :contents="article" />
    </div>
    <div id="pict-modal -pad-5per" class="modal" 
        v-bind:class="{
          'is-active': isModal,
          '-pad-5per': yesSaitoKyouko
          }">
      <div class="modal-background" @click="modalControl(null, false)"></div>
      <div v-if="notSaitoKyouko" class="modal-content" @click="modalControl(null, false)">
        <p class="image">
          <img :src="selectImage" alt="">
        </p>
      </div>
      <div v-if="yesSaitoKyouko" class="modal-content is-flex">
        <div class="info-area has-background-white-ter has-text-grey-dark">
          <information :profileImageUrl="profileImageUrl"/>
        </div>
      </div>
      <button class="modal-close is-large" aria-label="close"
        @click="modalControl(null, false)"></button>
    </div>
    <div class="self-info yesSaitouKyouko">
        <p class="button info-button is-paddingless is-marginless"
        @click="showInformation">
          <font-awesome-icon icon="paw" class="info-icon" />
        </p>
      </div>
  </main>
</template>

<script>
import ArticlePanel from "./article/ArticlePanel"
import Information from './Information'

export default {
  name: "main-contents",
  props: [
    "articleData"
  ],
  components:{
    ArticlePanel,
    Information
  },
  data() {
    return {
      errorMessage: "",
      isFilterd: false,
      selectImage: null,
      isModal: false,
      yesSaitoKyouko: false,
      notSaitoKyouko: true,
      profileImageUrl: ""
    }
  },
  mounted() {
    if (this.articleData && this.profileImageUrl === "") {
      this.profileImageUrl = this.articleData[0].profImage
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
        this.yesSaitoKyouko = false
        this.notSaitoKyouko = true
      }
    },
    showInformation: function () {
      this.yesSaitoKyouko = true
      this.notSaitoKyouko = false
      this.modalControl(null, true)
    }
  }
}
</script>

<style lang="scss" scoped>
.main-contents {
  padding: 10px 0; 
  background-color: rgb(240, 248, 239);
}
.-pad-5per {
  padding: 5%;
}
.modal {
  z-index: 100;
}
.modal-content {
  width: 100%;
  max-height: 90%;
}
.info-button {
  background-color: rgba(41, 175, 86, 0.418);
  .info-icon {
    color: #fbfd75;
  }
}
.info-area {
  overflow: scroll;
  width: 100%;
}
.info-inner-area {
  width: 100%;
  height: 100%;
}
.yesSaitouKyouko {
  color: white;
  background-color: white;
}
@media screen and (min-width : 300px){
  .content-area {
    padding: 0 10%;
  }
  .self-info {
    position: fixed;
    bottom: 4%;
    p {
      width: 1.8em;
    }
  }
  .info-icon {
    font-size: 0.9em;
  }
}
@media screen and (min-width : 720px){
  .content-area {
    padding: 0 20%;
    margin-bottom: 50px;
  }
  .self-info {
    position: fixed;
    bottom: 8%;
    p {
      width: 2.2em;
    }
  }
  .info-icon {
    font-size: 1.3em;
  }
}
@media screen and (min-width : 1600px){
  .content-area {
    padding: 0 30%;
    margin-bottom: 50px;
  }
  .self-info {
    position: fixed;
    bottom: 6%;
    p {
      width: 3.1em;
    }
  }
}
</style>
