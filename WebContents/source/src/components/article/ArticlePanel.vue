<template>
<div id="article-panel" class="article-panel">
  <div class="card">
    <header class="card-header is-flex">
      <figure class="image is-48x48">
        <img class=" is-rounded" :src="contents.imageUrl">
      </figure>
      <p class="card-header-title">
        {{ authorName }}
      </p>
    </header>
    <div class="card-image">
      <figure class="image">
        <img :src="contents.imageUrl"
          @click="modalControl(contents.imageUrl, true)">
      </figure>
    </div>
    <div class="card-content">
      <div class="media">
        <div class="media-left">

        </div>
      </div>
      <div class="content has-text-left">
        <pre class="is-paddingless has-background-white">{{contents.text}}</pre>
        <a class="is-size-7 is-marginless is-block" 
          v-for="(tag, index) in contents.tagList" v-bind:key="index">
          {{tag}}</a>
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
      isFilterd: false,
      isModal: false,
      selectImageUrl: ''
    }
  },
  methods: {
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
</style>
