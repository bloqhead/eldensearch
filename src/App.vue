<template>
  <main>
    <div class="search-wrap">
      <div class="page-header">
        <div>
          <h1>Elden Ring Weapon Search</h1>
        </div>
        <div>
          <ul class="menu">
            <li><a href="https://github.com/bloqhead/demigods" target="_blank">Demigods API</a></li>
            <li><a href="https://github.com/bloqhead/eldensearch/compare" target="_blank">Contribute</a></li>
          </ul>
        </div>
      </div>
      <search
        v-model="query"
        :items="categories"
        @search="runSearch"
        @pick-category="fetchByCategory"
      />
      <pagination
        :page-number="pageNumber"
        :page-count="pageCount"
        @next-page="nextPage"
        @prev-page="prevPage"
      />
    </div>
    <div class="list-wrap">
      <list
        :loading="loading"
        :items="filteredItems"
        @retry="fetchAll"
      />
      <div class="mt-2 md:mt-4">
        <pagination
          :page-number="pageNumber"
          :page-count="pageCount"
          @next-page="nextPage"
          @prev-page="prevPage"
        />
      </div>
    </div>
    <div class="page-footer">
      <div>
        <p>Elden Ring is property of <a href="https://www.bandainamcoent.com/" target="_blank">Bandai Namco</a>. This project is unofficial.</p>
      </div>
    </div>
  </main>
</template>

<script setup lang="ts">
import { onMounted, ref, computed } from 'vue'
import type { Ref } from 'vue'
import type { Weapon } from './types'
import Search from './components/Search.vue'
import List from './components/List.vue'
import Pagination from './components/Pagination.vue'

const rand: Ref = ref<String>('')
const query: Ref = ref<String>('')
const categories: Ref = ref<Ref[]>([])
const items: Ref = ref<Ref[]>([])
const error: Ref = ref<Boolean>(false)
const loading: Ref = ref<Boolean>(true)
const pageSize: Ref = ref<Number>(12)
const pageNumber: Ref = ref<Number>(0)

const api = 'https://demigods-golang.vercel.app/api'
const categoriesEndpoint = `${api}/categories`

const filteredItems = computed(() => {
  const filter = query.value
  const start = pageNumber.value * pageSize.value
  const end = start + pageSize.value

  if (!filter.length) {
    return items.value?.slice(start, end)
  }

  return items.value.filter((i: Weapon) => {
    return i.weapon.toLowerCase().includes(filter.toLowerCase())
  }).slice(start, end)
})

const pageCount = computed(() => {
  const count = items.value?.length
  const size = pageSize.value

  return Math.ceil(count / size)
})

const prevPage = () => {
  if(pageNumber.value > 0) {
    pageNumber.value = pageNumber.value - 1 
  } else {
    pageNumber.value = 0
  }
}

const nextPage = () => {
  if(pageNumber.value < pageCount.value -1) {
    pageNumber.value = pageNumber.value + 1
  }
}

const runSearch = (ev: string) => {
  query.value = ev
}

const fetchCategories = async () => {
  pageNumber.value = 0

  await fetch(categoriesEndpoint)
    .then((res) => res.json())
    .then((data) => categories.value = data)
}

const fetchAll = async () => {
  loading.value = true
  pageNumber.value = 0

  await fetch(`${api}/all`)
    .then((res) => res.json())
    .then((data) => {
      if (data && data.length > 0) {
        items.value = data
      } else {
        items.value = []
        error.value = true
      }

      loading.value = false
    })
}

const fetchByCategory = async (cat: String) => {
  loading.value = true
  pageNumber.value = 0

  await fetch(`${api}/category/${cat}`)
    .then((res) => res.json())
    .then((data) => {
      if (data && data.length > 0) {
        items.value = data
      } else {
        items.value = []
        error.value = true
      }

      loading.value = false
    })
}

onMounted(() => {
  fetchAll()
  fetchCategories()
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

.page-header {
  @apply
    flex
    flex-col
    sm:flex-row
    items-center
    justify-between
    p-2
    sm:p-4
    rounded-md
    bg-slate-900;
}

.page-header h1 {
  @apply
    font-serif
    font-normal
    text-base
    md:text-xl
    text-emerald-500;
}

.page-header .menu {
  @apply
    flex
    items-center
    gap-4
    text-sm;
}

.page-header .menu a {
  @apply block;
}

.page-footer {
  @apply
    p-4
    mt-4
    border-t
    border-slate-800
    text-center
    text-xs
    text-slate-500;
}

.search-wrap {
  @apply
    flex
    flex-col
    gap-2
    md:gap-4
    sticky
    z-10
    top-0
    p-4
    mb-4
    bg-slate-800
    rounded-xl;
}
</style>