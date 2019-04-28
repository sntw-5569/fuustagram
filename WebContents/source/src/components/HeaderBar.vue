<template>
  <header class="header-bar">
    <nav class="level is-flex">
      <div class="level-left title-logo">
        <figure class="image is-4by1">
          <a href="/" class="is-inline">
            <img src="../assets/fuusta_logo.png" href="/">
          </a>
        </figure>
      </div>
      <div class="level-right is-flex">
        <div class="level-item control has-icons-left">
          <input class="input serch-input" type="text" placeholder="keyword">
            <span class="icon is-small is-left input-innner">
              <font-awesome-icon icon="search" class="input-innner-icon"/>
          </span>
        </div>
        <div class="level-item head-icon">
          <font-awesome-icon icon="sync-alt" />
        </div>
        <div class="level-item head-icon">
          <font-awesome-icon icon="arrow-alt-circle-up" />
        </div>
      </div>
    </nav>
  </header>
</template>

<script>
export default {
  name: "haeder-bar",
  data() {
    return {
      errorMessage: "",
      isFilterd: false,
    }
  },
  methods: {
  }
}
</script>

<style lang="scss" scoped>
.header-bar {
  position: sticky;
  top: 0;
  overflow: hidden;
  background-color: white;
  // border-bottom: solid 1px rgb(150, 150, 150);
  box-shadow: 1px 2px 3px 0px #bbb;
  z-index: 1;
}
.level-item {
  margin: 0;
}
.input {
    color: darkred;
    background-color: rgb(238, 238, 238);
    font-size: small;
}
.input-innner-icon {
  color: slategray;
}

@media screen and (min-width : 300px){
  nav.level {
    padding: 0;
    margin: 0;
  }
  .level-right {
    width: 60%;
    margin: 0;
    div {
      padding: 2px;
    }
  }
  .input {
    width: 100%;
  }
  div.control {
    width: 80%;
  }

  .title-logo {
    width: 30%;
    img {
      width: 100%;
    }
  }
  .head-icon {
    font-size: 22px;
  }
}

@media screen and (min-width : 720px){
  div.level-right {
    padding-top: 5px;
  }
  .title-logo {
    width: 30%;
    max-width: 200px
    img {
      width: 100%;
      margin: 10px;
    }
  }
  .head-icon {
    font-size: 35px;
  }
  .level-right {
    width: 60%;
    margin: 0;
    div {
      padding: 2px;
    }
  }
  .input {
    width: 100%;
  }
  div.control {
    width: 80%;
  }
}

</style>
