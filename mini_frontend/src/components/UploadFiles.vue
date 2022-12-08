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

    <a-table
      class="ant-table-striped"
      size="middle"
      :columns="columns"
      :data-source="data"
      :row-class-name="(_record, index) => (index % 2 === 1 ? 'table-striped' : null)"
    />
  </template>


<script>
import axios from "axios";
import { defineComponent } from 'vue';

export default {
  name: "upload-image",
  
  data() {
    
    return {
      columns : [
        { title: 'ImageName', dataIndex: 'imageName' },
        { title: 'caption', dataIndex: 'caption'},
        { title: 'ImageSize', dataIndex: 'imageSize' },
        { title: 'RTT', dataIndex: 'rtt' },
        { title: 'Throughput', dataIndex: 'throughput'},
      ],
      data : [
        {
          key: '1',
          name: 'John Brown',
          age: 32,
          address: 'New York No. 1 Lake Park',
        },
      ],

      selectedFiles: undefined,
      progressInfos: [],
      message: "",
      fileInfos: [],
      currentImage: undefined,

      caption: "nope",
      dataSource: []

    };
  },
  methods: {

    selectImage() {
      this.currentImage = this.$refs.file.files.item(0);
      this.previewImage = URL.createObjectURL(this.currentImage);
      this.progress = 0;
      this.message = "";
    },

    upload() {
      this.progress = 0;
      this.fileParam = new FormData(); //创建form对象
      this.fileParam.append("file", this.currentImage);
      let that = this

      // time before: todo
      let time_before = new Date().getTime();

      axios
        .post("http://192.86.139.93:8080/upload", this.fileParam)
        .then((response) => {
            let rtt = new Date().getTime() - time_before;
            console.log(response.data);
            that.data.push({
              imageName : that.currentImage.name,
              caption : response.data,
              imageSize : that.currentImage.size,
              rtt : rtt + "ms",
              throughput : (that.currentImage.size/(rtt * 1024)) + "kb/s"
            })
        })
        .catch((e) => {
            console.log(e);
        });
      
    },
  },

  mounted() {
    // UploadService.getFiles().then(response => {
    //   this.imageInfos= response.data;
    // });
    var that = this
  },


};


</script>



<style>
.ant-table-striped :deep(.table-striped) td {
  background-color: #fafafa;
}
</style>