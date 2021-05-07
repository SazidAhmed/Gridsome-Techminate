<template>
  <Layout>
    <v-form>
      <v-container>
        <v-row>
          <v-col
            cols="12"
            sm="6"
          >
            <v-text-field
              v-model="first"
              label="First Name"
              outlined
              shaped
            ></v-text-field>
          </v-col>
        </v-row>
      </v-container>
    </v-form>
  </Layout>
</template>

<script>

export default {
  data: () => ({
      first: 'John',
    }),
  components:{
   
  },
  metaInfo: {
    title: 'Contact'
  }
}
</script>

<style>

</style>
