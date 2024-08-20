<template>
  <div style="padding: 20px">
    <!-- 标题 -->
    <p style="font-size: 29px; font-weight: bold; margin-bottom: 20px">
      👋 当前页面： [ 主力配置 ]
    </p>
    <p style="font-size: 20px; margin-bottom: 20px">
      🗨️ 根据模板 [点击] 进行选择，选中后可点击进行编辑。
    </p>
    <br />
    <!-- 模板列表 -->
    <el-divider content-position="left">
      <el-tag
        type="success"
        round
        style="font-size: 22px; background-color: #e0f7fa; color: #00796b"
      >
        模板列表：
      </el-tag>
    </el-divider>

    <!-- 表格 -->
    <el-table
      :data="tableData"
      highlight-current-row
      @row-click="handleRowClick"
      :current-row-key="selectedRowKey"
      class="custom-table"
      style="margin-bottom: 20px"
    >
      <el-table-column prop="id" label="ID" width="80" />
      <el-table-column prop="type" label="类型" width="120" />
      <el-table-column prop="name" label="主将" />
      <el-table-column prop="aos" label="兵种" width="100" />
      <el-table-column prop="level" label="等级" width="100" />
      <el-table-column prop="g1" label="副将1" />
      <el-table-column prop="g1_s1" label="副将1技能1" />
      <el-table-column prop="g1_s2" label="副将1技能2" />
      <el-table-column prop="g2" label="副将2" />
      <el-table-column prop="g2_s1" label="副将2技能1" />
      <el-table-column prop="g2_s2" label="副将2技能2" />
      <el-table-column prop="g3" label="副将3" />
      <el-table-column prop="g3_s1" label="副将3技能1" />
      <el-table-column prop="g3_s2" label="副将3技能2" />
    </el-table>
    
    <br />
    <!-- 编辑表单 -->
    <el-divider content-position="left">
      <el-tag
        type="success"
        round
        style="font-size: 22px; background-color: #e0f7fa; color: #00796b"
      >
        编辑表单:
      </el-tag>
    </el-divider>

    <!-- 编辑表单 -->
    <div v-if="selectedRow && Object.keys(selectedRow).length">
      <el-form
        :model="selectedRow"
        label-width="100px"
        style="font-size: 16px; max-width: 800px; margin: 0 auto"
      >
        <!-- 基本信息 -->
        <el-row style="margin-bottom: 15px">
          <el-col :span="6">
            <el-form-item label="ID" style="margin-bottom: 0">
              <el-input
                v-model="selectedRow.id"
                disabled
                style="max-width: 100%"
              />
            </el-form-item>
          </el-col>
          <el-col :span="6">
            <el-form-item label="主将" style="margin-bottom: 0">
              <el-input v-model="selectedRow.name" style="max-width: 100%" />
            </el-form-item>
          </el-col>
          <el-col :span="6">
            <el-form-item label="兵种" style="margin-bottom: 0">
              <el-input v-model="selectedRow.aos" style="max-width: 100%" />
            </el-form-item>
          </el-col>
          <el-col :span="6">
            <el-form-item label="等级" style="margin-bottom: 0">
              <el-input v-model="selectedRow.level" style="max-width: 100%" />
            </el-form-item>
          </el-col>
        </el-row>

        <!-- 副将1 -->

        <!-- <el-divider content-position="left" style="margin: 20px 0">
          <el-tag
            type="info"
            round
            style="font-size: 18px; background-color: #e3f2fd; color: #1e88e5"
          >
            副将1
          </el-tag>
        </el-divider> -->
        <br />
        <el-form-item label="副将1名称" style="margin-bottom: 10px">
          <el-input v-model="selectedRow.g1" style="max-width: 100%" />
        </el-form-item>
        <el-form-item label="副将1技能">
          <el-row style="align-items: center">
            <el-col :span="11" style="margin-right: 5px">
              <el-input
                v-model="selectedRow.g1_s1"
                placeholder="技能1"
                style="max-width: 100%"
              />
            </el-col>
            <el-col :span="11">
              <el-input
                v-model="selectedRow.g1_s2"
                placeholder="技能2"
                style="max-width: 100%"
              />
            </el-col>
          </el-row>
        </el-form-item>

        <!-- 副将2 -->
        <!-- <el-divider content-position="left" style="margin: 20px 0">
          <el-tag
            type="info"
            round
            style="font-size: 18px; background-color: #e3f2fd; color: #1e88e5"
          >
            副将2
          </el-tag>
        </el-divider> -->
        <br />

        <el-form-item label="副将2名称" style="margin-bottom: 10px">
          <el-input v-model="selectedRow.g2" style="max-width: 100%" />
        </el-form-item>
        <el-form-item label="副将2技能">
          <el-row style="align-items: center">
            <el-col :span="11" style="margin-right: 5px">
              <el-input
                v-model="selectedRow.g2_s1"
                placeholder="技能1"
                style="max-width: 100%"
              />
            </el-col>
            <el-col :span="11">
              <el-input
                v-model="selectedRow.g2_s2"
                placeholder="技能2"
                style="max-width: 100%"
              />
            </el-col>
          </el-row>
        </el-form-item>

        <!-- 副将3 -->
        <!-- <el-divider content-position="left" style="margin: 20px 0">
          <el-tag
            type="info"
            round
            style="font-size: 18px; background-color: #e3f2fd; color: #1e88e5"
          >
            副将3
          </el-tag>
        </el-divider> -->
        <br />

        <el-form-item label="副将3名称" style="margin-bottom: 10px">
          <el-input v-model="selectedRow.g3" style="max-width: 100%" />
        </el-form-item>
        <el-form-item label="副将3技能">
          <el-row style="align-items: center">
            <el-col :span="11" style="margin-right: 5px">
              <el-input
                v-model="selectedRow.g3_s1"
                placeholder="技能1"
                style="max-width: 100%"
              />
            </el-col>
            <el-col :span="11">
              <el-input
                v-model="selectedRow.g3_s2"
                placeholder="技能2"
                style="max-width: 100%"
              />
            </el-col>
          </el-row>
        </el-form-item>
      </el-form>
      <br />
    </div>

    <!-- 未选择模板提示 -->
    <div v-else>
      <div>
        <p style="font-size: 24px; color: #ff5722; text-align: center">
          ！！！未选择任何模板，请先选择一个模板。
        </p>
      </div>
    </div>

    <!-- 发送按钮 -->
    <el-button
      type="primary"
      :disabled="!selectedRow"
      @click="post"
      style="font-size: 18px; margin-top: 20px"
    >
      ✈ 发送配置信息
    </el-button>
  </div>
</template>

<script>
import { fetchData, postDate } from "../api";

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
      this.tableData = response.data;
    },

    handleRowClick(row) {
      this.selectedRow = { ...row };
      this.selectedRowKey = row.id;
    },

    post() {
      postDate(this.selectedRow).then((res) => {
        console.log("res", res.data.msg);
        if (res.data.msg === "success") {
          ElNotification({
            title: "Success",
            message: "配置结果保存成功！",
            type: "success",
          });
        } else {
          ElNotification({
            title: "Error",
            message: "配置结果保存失败！",
            type: "error",
          });
        }
      });
    },
  },
  mounted() {
    this.getData();
  },
};
</script>

<style scoped>
.custom-table {
  font-size: 14px;
}

.el-table th,
.el-table td {
  padding: 8px 12px;
}

.el-form-item {
  margin-bottom: 10px;
}

.el-form-item label {
  font-size: 16px;
}

.el-input {
  font-size: 16px;
}

.el-button {
  font-size: 18px;
}
</style>
