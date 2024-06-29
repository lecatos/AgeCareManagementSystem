<script setup lang="ts">
import axios from "axios";
function submits(e: any){
      let myForm = document.getElementById('staffadd') as HTMLFormElement; 
         let formData = new FormData(myForm);
         const data = {}; 
         // need to convert it before using not with XMLHttpRequest
         for (let [key, val] of formData.entries()) {
               Object.assign(data, {[key]: val})
         }
         console.log(data);
         axios.post(e.target.action, formData).then(function (response) {
            alert("Sucess!")
        }).catch((res)=>{
          console.log(res);
          alert("Failed!\nReason:" + JSON.stringify(res.response.data, null, "\t"))
        });
    }
</script>

<template>
  <div class="staffAdd">
      <h2>This is a Staff Add page</h2>
      
      <form v-on:submit.prevent="submits" id="staffadd" method="post" action="/api/user/register">
          <!-- File Upload -->
          <div class="form-group">
              <label for="photo">Upload Photo</label>
              <input id="photo" type="file" name="avatar">
          </div>
          <!-- Full Name -->
          <div class="form-group">
              <label for="fname">First Name</label>
              <input id="fname" type="text" name="first_name">
          </div>
          <div class="form-group">
              <label for="lname">Last name</label>
              <input id="lname" type="text" name="last_name">
          </div>
          <div class="form-group">
              <label for="username">Username</label>
              <input id="username" type="text" name="username">
          </div>
          <div class="form-group">
              <label for="password">Password</label>
              <input id="password" type="password" name="password">
          </div>
          <!-- Gender Selection -->
          <div class="form-group gender">
                <span>Gender:</span>
                <div>
                    <input type="radio" id="male" name="sex" value="M" class="gender-radio">
                    <label for="male" class="gender-label">Male</label>
                    
                    <input type="radio" id="female" name="sex" value="F" class="gender-radio">
                    <label for="female" class="gender-label">Female</label>
                </div>
          </div>
          <!-- Job Role -->
          <div class="form-group">
              <label for="job">Job Role</label>
              <input id="job" type="text" name="job">
          </div>
          <!-- Email -->
          <div class="form-group">
              <label for="email">Email</label>
              <input id="email" type="text" placeholder="david@hotmail.com" name="email">
          </div>
          <!-- Phone Number -->
          <div class="form-group">
              <label for="phoneno">Phone Number</label>
              <input id="phoneno" type="text" name="tel">
          </div>
          <!-- Staff ID -->
          <div class="form-group">
              <label for="sID">Staff ID</label>
              <input id="sID" type="text" name="sID">
          </div>
          <!-- Date of Birth -->
          <div class="form-group">
              <label for="DoB">Date of Birth</label>
              <input type="date" id="DoB" name="dob">
          </div>
          <!-- Certification -->
          <div class="form-group">
              <label for="cert">Certification</label>
              <select name="certification" id="cert">
                  <option value="Certificate IV in Managing">Certificate IV in Managing</option>
                  <option value="Certificate V in Human Resources">Certificate V in Human Resources</option>
                  <option value="MBA">MBA</option>
                  <option value="Other">Other</option>
              </select>
          </div>
          <!-- Insurance No -->
          <div class="form-group">
              <label for="insuranceno">Insurance No.</label>
              <input id="insuranceno" type="text" name="insuranceno">
          </div>
          <!-- Emergency Contact -->
          <div class="form-group">
              <label for="emergencycontact">Emergency Contact</label>
              <input id="emergencycontact" type="text" name="emergencycontact">
          </div>
          <!-- Payment Details -->
          <div class="form-group">
              <label for="payinfo">Payment Details</label>
              <input id="payinfo" type="text" name="payinfo">
          </div>
          <!-- Document -->
          <div class="form-group">
              <label for="document">Document</label>
              <input id="document" type="text" name="document">
          </div>
          <!-- Special Notes -->
          <div class="form-group">
              <label for="notes">Special Notes</label>
              <input id="notes" type="text" name="notes">
          </div>
          <!-- Form Buttons -->
          <div class="form-buttons">
              <input type="submit" value="Submit" class="button">
              <input type="reset" value="Reset" class="button">
          </div>
      </form>
  </div>
</template>

<style scoped>
.staffAdd {
    font-family: Arial, sans-serif;
    max-width: 600px;
    margin: auto;
    padding: 20px;
    box-shadow: 0 0 10px rgba(0,0,0,0.1);
    background: #f9f9f9;
    border-radius: 8px;
}

.staffAdd h2 {
    text-align: center;
    color: #333;
}

.form-group {
    margin-bottom: 15px;
}

.form-group label {
    margin-bottom: 5px;
    font-weight: bold;
    color: #666;
}

.form-group input[type="text"],
.form-group input[type="date"],
.form-group select {
    width: 100%;
    padding: 8px;
    border: 1px solid #ccc;
    border-radius: 4px;
}

.form-group input[type="radio"] {
    margin-right: 5px
}

/* Gender Selection Styling */
.gender-radio {
    display: none; /* Hide the default radio button */
}

.gender-label {
    display: inline-block;
    text-align: center;
    width: 15%;
    padding: 8px 15px;
    background-color: #f2f2f2;
    border: 2px solid #d1d1d1;
    border-radius: 4px;
    margin-right: 10px;
    cursor: pointer;
    transition: background-color 0.2s, color 0.2s;
}

.gender-radio:checked + .gender-label {
    background-color: #007bff;
    color: white;
    border-color: #0056b3;
}

.gender-label:hover {
    background-color: #e7e7e7;
}

/* Submit and Reset Buttons Styling */
.form-buttons .button {
    padding: 10px 20px;
    margin-right: 10px;
    border: none;
    border-radius: 4px;
    background-color: #0056b3;
    color: white;
    cursor: pointer;
}

.form-buttons .button:hover {
    background-color: #004494;
}

.form-buttons .button.reset {
    background-color: #cccccc;
    color: #333;
}
</style>
