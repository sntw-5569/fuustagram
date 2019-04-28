<template>
  <footer class="footer-menu">
    <div class="level is-flex">
      <div class="footer-text">
        <h4>Created by Shinotatwu.</h4>
        <small>©︎2019 Fuustagram. Contents from Photo and text a royalty by the Fuyuka Saito, and Seed&Flower LLC Right reserved.</small>
      </div>
    </div>
  </footer>
</template>

<script>
export default {
  name: "footer-menu",
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
.footer-menu {
  bottom: 0px;
  width: 100%;
  border-top: solid 1px #aaa;
  background-color: #eee;
}
.footer-text {
  width: 100%;
  padding: 0;
  h4 {
    padding: 0;
  }
  small {
    margin: 15px 0;
  }
}

@media screen and (min-width : 300px){
  .footer-menu {
    position: relative;
  }
}
@media screen and (min-width : 720px){
  .footer-menu {
    position: fixed;
  }
}

</style>