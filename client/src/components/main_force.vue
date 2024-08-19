<template>
  <div>
    <br />
    <p>-- 当前页面>>> zhuli配置</p>
    <p>🗨️🗨️ 根据模板 [点击] 进行选择，选中后点击《发送配置结果》按钮!</p>
    <br />
    <el-divider content-position="left"
      ><el-tag type="success" round>模板列表：</el-tag></el-divider
    >
    <el-table
      :data="tableData"
      style="width: 100%"
      @row-click="handleRowClick"
      :current-row-key="selectedRowKey"
    >
      <el-table-column prop="mingcheng" label="mingcheng" />
      <el-table-column prop="bingzhong" label="bingzhong" />
      <el-table-column prop="dengji" label="dengji" />
      <el-table-column prop="zhujiang" label="zhujiang" />
      <el-table-column prop="jineng1" label="jineng1" />
      <el-table-column prop="jineng2" label="jineng2" />
      <el-table-column prop="fujiang1" label="fujiang" />
      <el-table-column prop="jineng1" label="jineng1" />
      <el-table-column prop="jineng2" label="jineng2" />
      <el-table-column prop="fujiang2" label="fujiang2" />
      <el-table-column prop="jineng1" label="jineng1" />
      <el-table-column prop="jineng2" label="jineng2" />
    </el-table>

    <br /><br />
    <div>
      <el-divider content-position="left"
        ><el-tag type="success" round>选中模板：</el-tag></el-divider
      >

      <div v-if="selectedRow && Object.keys(selectedRow).length">
        <el-table :data="[selectedRow]" style="width: 100%; margin-top: 20px">
          <el-table-column prop="mingcheng" label="mingcheng" />
          <el-table-column prop="bingzhong" label="bingzhong" />
          <el-table-column prop="dengji" label="dengji" />
          <el-table-column prop="zhujiang" label="zhujiang" />
          <el-table-column prop="jineng1" label="jineng1" />
          <el-table-column prop="jineng2" label="jineng2" />
          <el-table-column prop="fujiang1" label="fujiang" />
          <el-table-column prop="jineng1" label="jineng1" />
          <el-table-column prop="jineng2" label="jineng2" />
          <el-table-column prop="fujiang2" label="fujiang2" />
          <el-table-column prop="jineng1" label="jineng1" />
          <el-table-column prop="jineng2" label="jineng2" />
        </el-table>
      </div>
      <div v-else>
        <el-alert
          title="未选择任何模板，请先选择一个模板。"
          type="warning"
          show-icon
        />
      </div>
    </div>

    <br /><br />

    <el-button type="primary" :disabled="!selectedRow" @click="post">
      🚀 发送配置结果
    </el-button>
  </div>
</template>

<script>
import { fetchData } from "../api";

export default {
  data() {
    return {
      tableData: [],
      selectedRowKey: null,
      selectedRow: null,
    };
  },
  methods: {
    async getData() {
      const response = await fetchData();
      console.log("response:", response);
      this.tableData = response.data;
    },

    handleRowClick(row) {
      this.selectedRow = row;
      this.selectedRowKey = row.date;
    },

    post() {
      ElMessage.success("结果发送成功！");
    },
  },
  mounted() {
    this.getData();
  },
};
</script>
