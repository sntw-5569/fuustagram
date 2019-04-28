<template>
<div id="article-panel">
  <div class="n-row article-panel">
    <picture class="n-aspect">
      <img :src="imageUrl">
    </picture>
  </div>
</div>
</template>

<script>
export default {
  name: "article-panel",
  props: [
    "imageUrl"
  ],
  data() {
    return {
      errorMessage: '',
      isFilterd: false,
    }
  },
  methods: {
  }
}
</script>

<style lang="scss" scoped>
.article-panel {
  picture {
    --width: 400;
    --height: 150;
  }
}
</style>
