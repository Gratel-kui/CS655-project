<template>
    <div>
      <div class="row">
        <div class="col-8">
          <label class="btn btn-default p-0">
            <input
              type="file"
              accept="image/*"
              ref="file"
              @change="selectImage"
            />
          </label>
        </div>
        <div class="col-4">
          <button
            class="btn btn-success btn-sm float-right"
            :disabled="!currentImage"
            @click="upload"
          >
            upload
          </button>
        </div>
      </div>
      <div v-if="currentImage" class="progress">
        <div
          class="progress-bar progress-bar-info"
          role="progressbar"
          :aria-valuenow="progress"
          aria-valuemin="0"
          aria-valuemax="100"
          :style="{ width: progress + '%' }"
        >
          {{ progress }}%
        </div>
      </div>
      <div v-if="previewImage">
        <div>
          <img class="preview my-3" :src="previewImage" alt="" />
        </div>
      </div>
      <div v-if="message" class="alert alert-secondary" role="alert">
        {{ message }}
      </div>

      <div>
        image caption by clip_pre: {{caption}}
      </div>


      <!-- <el-table
        :data="tableData"
        style="width: 100%">
        <el-table-column
          prop="date"
          label="日期"
          width="180">
        </el-table-column>
        <el-table-column
          prop="name"
          label="姓名"
          width="180">
        </el-table-column>
        <el-table-column
          prop="address"
          label="地址">
        </el-table-column>
      </el-table> -->

      <div class="card mt-3">
        <div class="card-header">图片列表</div>
        <ul class="list-group list-group-flush">
          <li
            class="list-group-item"
            v-for="(image, index) in imageInfos"
            :key="index"
          >
            <a :href="image.url">{{ image.name }}</a>
          </li>
        </ul>
      </div>
    </div>
  </template>


<script>
import axios from "axios";
import UploadService from "../services/UploadFilesService";
export default {
  name: "upload-image",
  data() {

    return {
      selectedFiles: undefined,
      progressInfos: [],
      message: "",
      fileInfos: [],
      currentImage: undefined,

      caption: "nope",

      tableData: [{
            date: '2016-05-02',
            name: '王小虎',
            address: '上海市普陀区金沙江路 1518 弄'
          }, {
            date: '2016-05-04',
            name: '王小虎',
            address: '上海市普陀区金沙江路 1517 弄'
          }, {
            date: '2016-05-01',
            name: '王小虎',
            address: '上海市普陀区金沙江路 1519 弄'
          }, {
            date: '2016-05-03',
            name: '王小虎',
            address: '上海市普陀区金沙江路 1516 弄'
          }]
    };
  },
  methods: {

    selectImage() {
      this.currentImage = this.$refs.file.files.item(0);
      this.previewImage = URL.createObjectURL(this.currentImage);
      this.progress = 0;
      this.message = "";
      data.currentImage = this.currentImage
    },

    upload() {
      this.progress = 0;
      this.fileParam = new FormData(); //创建form对象
      this.fileParam.append("file", this.currentImage);
      let that = this

      // time before: todo
      var time_before =

      axios
        .post("http://127.0.0.1:5000/upload", this.fileParam)
        .then((response) => {
            console.log(response.data);
            this.fileList = [];
            that.caption = response.data
        })
        .catch((e) => {
            console.log(e);
        });
      
      // todo: 
      // var time_after = 
      // rtt = ....

      // todo: calculate throughput
      


      
    //   UploadService.upload(this.currentImage)
    //     .then((response) => {
    //       this.message = response.data.message;
    //       return UploadService.getFiles();
    //     })
    //     .then((images) => {
    //       this.imageInfos = images.data;
    //     })
    //     .catch((err) => {
    //       this.progress = 0;
    //       this.message = "Could not upload the image! " + err;
    //       this.currentImage = undefined;
    //     });
    },
  },

  mounted() {
    UploadService.getFiles().then(response => {
      this.imageInfos= response.data;
    });
  },


};


</script>



<style>
/* body {
  font-family: Helvetica Neue, Arial, sans-serif;
  font-size: 14px;
  color: #444;
}

table {
  border: 2px solid #42b983;
  border-radius: 3px;
  background-color: #fff;
}

th {
  background-color: #42b983;
  color: rgba(255,255,255,0.66);
  cursor: pointer;
  -webkit-user-select: none;
  -moz-user-select: none;
  -user-select: none;
}

td {
  background-color: #f9f9f9;
}

th, td {
  min-width: 120px;
  padding: 10px 20px;
}

th.active {
  color: #fff;
}

th.active .arrow {
  opacity: 1;
}

.arrow {
  display: inline-block;
  vertical-align: middle;
  width: 0;
  height: 0;
  margin-left: 5px;
  opacity: 0.66;
}

.arrow.asc {
  border-left: 4px solid transparent;
  border-right: 4px solid transparent;
  border-bottom: 4px solid #fff;
}

.arrow.dsc {
  border-left: 4px solid transparent;
  border-right: 4px solid transparent;
  border-top: 4px solid #fff;
}

#search {
  margin-bottom: 10px;
} */
</style>