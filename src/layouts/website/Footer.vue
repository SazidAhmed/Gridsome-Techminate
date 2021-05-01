<template>
    <div>
        <v-footer color="deep-orange darken-3" class="hidden-sm-and-down py-4 white--text" >
            <div class="container">
                <v-row
                justify="center"
                no-gutters
                >
                  <g-link to="/" style="text-decoration: none;"><v-btn color="white" text rounded>Home</v-btn></g-link>
                  <g-link to="/about" style="text-decoration: none;"><v-btn color="white" text rounded>About</v-btn></g-link>
                  <g-link to="/service" style="text-decoration: none;"><v-btn color="white" text rounded>Services</v-btn></g-link>
                  <g-link to="/portfolio" style="text-decoration: none;"><v-btn color="white" text rounded>Portfolio</v-btn></g-link>
                  <g-link to="/testimonial" style="text-decoration: none;"><v-btn color="white" text rounded>Testimonial</v-btn></g-link>
                  <g-link to="/team" style="text-decoration: none;"><v-btn color="white" text rounded>Team</v-btn></g-link>
                  <g-link to="/contact" style="text-decoration: none;"><v-btn color="white" text rounded>Contact</v-btn></g-link>
                </v-row>
            </div>
        </v-footer>
        <div class="deep-orange darken-2 py-4 text-center white--text">
            <span>Copyright © Techminate {{ new Date().getFullYear() }}</span>
        </div>
  </div>
</template>

<script>
  export default {
    data: () => ({
     
    }),
  }
</script>

<style>

</style>