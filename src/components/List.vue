<template>
  <div class="list">
    <loading v-if="loading" @retry="$emit('retry')" />
    <ul
      v-else-if="loading === false && (items && items.length > 0)"
      class="list-items"
    >
      <li
        v-for="(item, idx) in items"
        :key="item.id"
        :data-index="idx"
        :style="`--i: ${idx}`"
      >
        <header>
          <div class="title-wrap">
            <h3 class="title">
              {{ item.name }}
            </h3>
            <h4 class="sub-title" title="Attack">
              <span>
                <fa :icon="['fasr', 'sword']" />
              </span>
              <span>
                {{ item?.skill ? item.skill : 'None' }}
              </span>
            </h4>
          </div>
          <div
            v-if="item.tier"
            class="tier"
          >
            {{ item.tier }}
          </div>
        </header>
        <div class="content">
          <div class="scaling">
            <h4 class="section-title">
              Scaling
            </h4>
            <ul v-if="item.scaling && Object.entries(item.scaling).length > 0">
              <li
                v-for="(value, label) in item.scaling"
                :key="label"
              >
                <h5
                  v-if="label"
                  class="scaling-label"
                >
                  {{ label }}
                </h5>
                <p
                  v-if="value"
                  class="scaling-value"
                >
                  {{ value }}
                </p>
              </li>
            </ul>
            <empty v-else>
              <p>No Scaling data.</p>
            </empty>
          </div>
          <div>
            <h4 class="section-title">
              Stats
            </h4>
            <div
              v-if="item.stats && Object.entries(item.stats).length > 0"
              class="stats"
            >
              <ul>
                <li
                  v-for="(value, stat) in item.stats"
                  :key="stat"
                  class="stat"
                >
                  <span>
                    <fa
                      v-if="iconHandler(stat).length > 0"
                      :icon="iconHandler(stat)"
                    />
                  </span>
                  <span :class="{ 'is-null': value === 0 }">
                    {{ value }}
                  </span>
                </li>
              </ul>
            </div>
            <empty v-else>
              <p>No Stats data.</p>
            </empty>
          </div>
        </div>
      </li>
    </ul>
    <empty v-else>
      <p>No items found.</p>
    </empty>
  </div>
</template>

<script setup lang="ts">
import Empty from './Empty.vue'
import Loading from './Loading.vue'

defineProps({
  items: {
    type: Object,
    required: false,
  },
  loading: {
    type: Boolean,
    default: true,
  },
})

const iconHandler = (name: String | Number) => {
  let icon: String | Number = name !== undefined ? name : ''!

  switch(name.toString().toLowerCase()) {
    case 'weight' :
      icon = 'weight-hanging'
      break
    case 'physical' :
      icon = 'sword'
      break
    case 'magic' :
      icon = 'wand-magic-sparkles'
      break
    case 'fire' : 
      icon = 'fire'
      break
    case 'light' :
      icon = 'lightbulb'
      break
    case 'holy' :
      icon = 'book-bible'
      break
    default :
      icon = ''
  }

  return ['fasr', icon]
}
</script>

<style scoped>
.list {

}

.list-items {
  @apply
    flex
    flex-col
    gap-4
    md:grid
    md:grid-cols-2
    lg:grid-cols-3;
}

.title {
  @apply
    text-lg
    md:text-xl;
}

.sub-title {
  @apply
    flex
    items-center
    gap-2
    mt-2
    pt-2
    border-t
    border-t-slate-500
    font-serif
    text-sm
    text-slate-400
    lg:text-base;
}

.list-items header {
  @apply
    flex
    items-center
    gap-4
    px-6
    py-2
    bg-slate-700;
}

.list-items .tier {
  @apply
    font-serif
    text-xl
    bg-slate-800
    text-emerald-500
    px-3
    py-1
    rounded-md;
}

.list-items .title-wrap {
  @apply flex-1;
}

.list-items > li {
  @apply
    rounded-md
    overflow-hidden
    bg-slate-800;
}

.list-items .content {
  @apply
    p-6
    pt-2;
}

.scaling > ul {
  @apply
    w-full
    grid
    grid-flow-col
    auto-cols-fr
    items-center
    justify-center
    gap-4
    divide-x
    divide-slate-500
    text-center;
}

.scaling > ul > li {
  @apply p-2;
}

.scaling-label {
  @apply
    uppercase
    text-sm;
}

.scaling-value {
  @apply
    uppercase
    text-3xl
    font-serif
    text-emerald-500;
}

.section-title {
  @apply
    flex
    items-center
    gap-2
    font-serif
    text-sm
    text-slate-500
    font-thin
    tracking-widest
    uppercase
    my-2
    after:block
    after:flex-1
    after:h-[1px]
    after:bg-slate-500;
}

.stats > ul {
  @apply
    grid
    grid-cols-3
    gap-2
    text-center;
}

.stats > ul > li {
  @apply
    bg-slate-700
    rounded-lg
    flex
    items-center
    justify-center
    border-2
    border-slate-800;
}

.stats > ul > li span {
  @apply
    flex-1
    p-2
    first:border-r-2
    first:border-slate-800
    first:text-emerald-500
    last:font-mono;
}

.is-null {
  @apply text-slate-500;
}
</style>