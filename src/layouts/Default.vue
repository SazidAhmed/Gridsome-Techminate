<template>
  <v-app id="inspire">
    <!--Drawer Left-->
    <!-- <v-navigation-drawer app v-model="drawer" drawer width="300">
      <v-list dense>
      </v-list>
    </v-navigation-drawer> -->

    <!--Navbar-->
    <v-app-bar app color="rgba(241, 90, 34, 1)" flat>
      <div class="d-flex align-center">
        <v-app-bar-nav-icon @click.stop="drawer = !drawer" class="hidden-md-and-up"></v-app-bar-nav-icon>
        <g-link to="/" style="text-decoration: none;">
          <g-image src="~/assets/nav/techminate.png" width="264" height="22" class="mt-1"/>
        </g-link>
      </div>
      <v-spacer></v-spacer>
      <div class="hidden-sm-and-down">
        <g-link to="/" style="text-decoration: none;"><v-btn color="white" text rounded>Home</v-btn></g-link>
        <g-link to="/whychooseus" style="text-decoration: none;"><v-btn color="white" text rounded>Why Us</v-btn></g-link>
        <g-link to="/service" style="text-decoration: none;"><v-btn color="white" text rounded>Services</v-btn></g-link>
        <g-link to="/portfolio" style="text-decoration: none;"><v-btn color="white" text rounded>Portfolio</v-btn></g-link>
        <g-link to="/testimonial" style="text-decoration: none;"><v-btn color="white" text rounded>Testimonial</v-btn></g-link>
        <g-link to="/team" style="text-decoration: none;"><v-btn color="white" text rounded>Team</v-btn></g-link>
        <g-link to="/contact" style="text-decoration: none;"><v-btn color="white" text rounded>Contact</v-btn></g-link>
      </div>
    </v-app-bar>
    <!-- Main Content -->
    <v-main>
      <!-- Provides the application the proper gutter -->
      <!--router pages-->
      <div class="orange lighten-5">
        <slot/>
      </div>
    </v-main>
    <!-- Footer -->
      <Footer />
  </v-app>
</template>
<static-query>
query {
  metadata {
    siteName
  }
}
</static-query>
<script>
import Footer from '../layouts/website/Footer.vue'
export default {
  name: 'App',

  components: {
    Footer
  },
  data(){
    return{
     drawer: null,
     drawer: false,
    }
  },
};
</script>
<style >
</style>
