<template>
<div id="article-panel" class="article-panel">
  <div class="card">
    <header class="card-header is-flex">
      <figure class="profile-icon image is-48x48">
        <img class=" is-rounded" :src="contents.profImage">
      </figure>
      <p class="card-header-title">
        {{ authorName }}
      </p>
    </header>
    <div class="card-image">
      <div class="" v-bind:class="{'n-slider': contents.imageUrl.length > 1 }">
          <figure v-for="(img, index) in contents.imageUrl"
           :key="index" class="image">
            <img :src="img"
              @click="modalControl(img, true)">
          </figure>
      </div>
    </div>
    <div class="card-content">
      <div class="media">
        <div class="media-left">

        </div>
      </div>
      <div class="content has-text-left">
        <pre class="is-paddingless has-background-white">{{contents.text}}</pre>
        <a class="is-size-7 is-marginless is-block" @click="tagClick(tag)"
          v-for="(tag, index) in contents.tagList" v-bind:key="index">
          #{{tag}}</a>
      </div>
    </div>
    <div class="card-footer">
      <div class=" card-footer-item">
        <p class="is-size-7 is-marginless">#{{contents.number}}</p>
      </div>
      <div class=" card-footer-item">
        <p class="is-size-7 is-marginless">{{contents.datetime}}</p>
      </div>
    </div>
  </div>
</div>
</template>

<script>
export default {
  name: "article-panel",
  props: [
    "modalControl",
    "contents"
  ],
  data() {
    return {
      authorName: 'fuyuka_saito',
      errorMessage: '',
      isModal: false
    }
  },
  methods: {
    tagClick: function(tag) {
      let searchBox = document.getElementById('search-input')
      searchBox.value = tag
      if (this.$searchFunction != null) {
        this.$searchFunction({key: 'Enter'}, tag)
      }
      let clearButton = document.getElementById('input-clear')
      if (!'has-text-success'.match(clearButton.attributes.class.value)) {
        let setClass = clearButton.attributes.class.value
        clearButton.setAttribute('class', setClass + ' has-text-success')
      }
    }
  }
}
</script>

<style lang="scss" scoped>
.article-panel {
  display: block;
  margin: 10px 0;
}
.card-header-title {
  margin: 0;
}
.profile-icon {
  margin: 5px;
  padding: 5px;
}
@media screen and (min-width : 300px){
  .card-header-title {
    font-size: 1.15em;
  }
}
@media screen and (min-width : 720px){
  .card-header-title {
    font-size: 1.5em;
  }
}
</style>
