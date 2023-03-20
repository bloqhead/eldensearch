<template>
  <main>
    <div class="search-wrap">
      <search
        :items="categories"
        v-model="query"
        @search="runSearch"
        @pick-category="fetchByCategory"
      />
    </div>
    <div class="list-wrap">
      <list :items="filteredItems" />
    </div>
  </main>
</template>

<script setup lang="ts">
import { onMounted, ref, reactive, computed } from 'vue'
import type { Ref } from 'vue'
import Search from './components/Search.vue'
import List from './components/List.vue'

const query = ref<String>('')
const categories: Ref = ref<Ref>([])
const items: Ref = reactive<Ref>([])
const error = ref<Boolean>(false)

const api = 'https://demigods.vercel.app/v1'
const categoriesEndpoint = `${api}/categories`

const filteredItems = computed(() => {
  const filter = query.value

  if (!filter.length) {
    return items.value
  }

  return items.value.filter((i) => {
    return i.weapon.toLowerCase().includes(filter.toLowerCase())
  })
})

const runSearch = (ev: string) => {
  query.value = ev
}

const fetchCategories = () => {
  fetch(categoriesEndpoint)
    .then((res) => res.json())
    .then((data) => categories.value = data)
}

const fetchAll = () => {
  fetch(`${api}/all`)
    .then((res) => res.json())
    .then((data) => {
      if (data && data?.status === 'success') {
        items.value = data.data
      } else {
        items.value = []
        error.value = true
      }
    })
}

const fetchByCategory = (cat: String) => {
  fetch(`${api}/${cat}`)
    .then((res) => res.json())
    .then((data) => {
      if (data && data?.status === 'success') {
        items.value = data.data
      } else {
        items.value = []
        error.value = true
      }
    })
}

onMounted(async () => {
  await fetchAll()
  await fetchCategories()
})
</script>

<style scoped>
main {
  @apply
    relative
    container
    mx-auto
    p-4
    lg:p-6
    max-w-6xl;
}

.search-wrap {
  @apply
    sticky
    z-10
    top-0
    p-4
    mb-4
    bg-slate-800
    rounded-xl;
}
</style>