<template>
  <v-app>
    <v-navigation-drawer app clipped>
        <list />
      <!-- -->
    </v-navigation-drawer>
    
  </v-app>
</template>

<script>
import List from "./List.vue"
export default {
  components: {List},

  data: () => ({
    //
  }),
};
</script>
