<template>
    <!-- parent relative child absolute -->
    <v-container fluid class="bg">
      <v-row no-gutters class="pa-12">
        <v-col cols="12" sm="12" md="1" lg="2">
        </v-col>
        <v-col cols="12" sm="12" md="5" lg="4">
          <div class="pa-10 white--text text-uppercase hidden-sm-and-down">
            <p class="font-weight-medium text-h5">Secure and Clean Code</p>
            <p class="font-weight-medium text-h3 mt-10">We manage your all in</p>
            <p class="d-block font-weight-medium text-h3 mb-10">all digital services</p>
            <span class="font-weight-medium text-subtitle-1">We are leading technology solutions providing company</span>
            <span class="d-block font-weight-medium text-subtitle-1">all over the world doing over 5 years</span>
          </div>
           <div class="white--text text-uppercase hidden-md-and-up">
            <p class="font-weight-medium text-h5">Secure and Clean Code</p>
            <p class="font-weight-medium text-h3 mt-10">We manage your all in</p>
            <p class="d-block font-weight-medium text-h3 mb-10">all digital services</p>
            <span class="font-weight-medium text-subtitle-1">We are leading technology solutions providing company all over the world doing over 5 years</span>
          </div>
        </v-col>
        <v-col cols="12" sm="12" md="6" lg="4">
          <div class="text-center">
            <span class="hidden-sm-and-down">
              <g-image alt="home" src="~/assets/home/Rectangle.png" quality="90" width="550" height="500" fit="fill"/>
            </span>
            <span class="hidden-md-and-up">
              <g-image class="mt-5 mb-5" alt="home" src="~/assets/home/Rectangle.png" quality="90" width="300" height="300" fit="fill"/>
            </span>
          </div>
        </v-col>
      </v-row>
    </v-container>
</template>

<script>
export default {
  metaInfo: {
    title: 'Home'
  }
}
</script>

<style scoped>
.bg{
  background: linear-gradient(90deg, #FC575E 0%, #F7B42C 100%), #C4C4C4;
  border-radius: 0px 0px 300px 300px;
}
</style>
