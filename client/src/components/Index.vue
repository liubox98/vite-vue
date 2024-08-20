<template>
  <div style="width: 88%; margin: 0 auto">
    <el-menu
      :default-active="activeIndex"
      mode="horizontal"
      :ellipsis="false"
      @select="handleSelect"
    >
      <el-menu-item>
        <img
          src="https://cdn-cn.lingxigames.com/czwxoycwxs/s33year/logo.png"
          alt="Element logo"
        />
      </el-menu-item>
      <el-menu-item index="1" style="font-size: 18px">🚩主力</el-menu-item>
      <el-menu-item index="2" style="font-size: 18px">2.铺路</el-menu-item>
      <el-menu-item index="3" style="font-size: 18px">3.碰瓷</el-menu-item>
      <el-menu-item index="4" style="font-size: 18px">4.策略</el-menu-item>
      <el-menu-item index="5" style="font-size: 18px">5.器械</el-menu-item>
      <el-menu-item index="6" style="font-size: 18px">6.兑换</el-menu-item>
    </el-menu>

    <div v-show="activeIndex === '1'">
      <main_force />
    </div>
    <div v-show="activeIndex === '2'">
      <p>铺路内容</p>
    </div>
    <div v-show="activeIndex === '3'">
      <p>碰瓷内容</p>
    </div>
    <div v-show="activeIndex === '4'">
      <p>策略内容</p>
    </div>
    <div v-show="activeIndex === '5'">
      <p>器械内容</p>
    </div>
    <div v-show="activeIndex === '6'">
      <p>兑换内容</p>
    </div>
  </div>
</template>

<script lang="ts" setup>
import { ref } from "vue";

const activeIndex = ref("1");
const handleSelect = (key: string) => {
  activeIndex.value = key;
};
</script>
<style>
.el-menu--horizontal > .el-menu-item:nth-child(1) {
  margin-right: auto;
}
</style>