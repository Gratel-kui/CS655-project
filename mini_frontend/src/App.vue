
<template>
  <div id="app">
    <div class="container" style="width:900px">
      <div class="my-4">
        <h2>Image Upload Demo</h2>
        <h5>Please Select your pictures and upload.</h5>

      </div>
      <upload-image></upload-image>
    </div>
  </div>
</template>

<script>
import UploadImage from "./components/UploadFiles.vue";
export default {
  name: "App",
  components: {
    UploadImage
  }
};
</script>

<style scoped>
/* header {
  line-height: 1.5;
}

.logo {
  display: block;
  margin: 0 auto 2rem;
}

@media (min-width: 1024px) {
  header {
    display: flex;
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }

  .logo {
    margin: 0 2rem 0 0;
  }

  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }
} */
</style>
