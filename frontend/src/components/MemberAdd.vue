<script lang="ts">
import axios from "axios";
export default {
  methods: {
    submits(e: any){
      let myForm = document.getElementById('memberadd') as HTMLFormElement; 
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
  }

};
</script>

<template>
  <div class="memberAdd">
      <h2>This is a Member Add page</h2>
      
      <form v-on:submit.prevent="submits" id="memberadd" method="post" action="/api/client/add">
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
          <!-- Email -->
          <div class="form-group">
              <label for="email">Email Address</label>
              <input id="email" type="text" placeholder="salamanca@gmail.com" name="email">
          </div>
          <!-- Phone Number -->
          <div class="form-group">
              <label for="phoneno">Phone Number</label>
              <input id="phoneno" type="text" name="tel">
          </div>
          <!-- Member ID -->
          <div class="form-group">
              <label for="mID">Member ID</label>
              <input id="mID" type="text" name="mID">
          </div>
          <!-- Date of Birth -->
          <div class="form-group">
              <label for="DoB">Date of Birth</label>
              <input type="date" id="DoB" name="dob">
          </div>
          <!-- Mailing Address -->
          <div class="form-group">
              <label for="mailingaddress">Mailing Address</label>
              <input id="mailingaddress" type="text" name="mailingaddress">
          </div>
          <!-- Membership Type -->
          <div class="form-group">
              <label for="membertype">Membership Type</label>
              <select name="membership" id="membertype">
                  <option value="Standard, $2000/Month">Standard, $2000/Month</option>
                  <option value="Standard Plus, $2500/month">Standard Plus, $2500/month</option>
                  <option value="Premium, $3500/month">Premium, $3500/month</option>
                  <option value="Ultra Premium, $5000/month">Ultra Premium, $5000/month</option>
              </select>
          </div>
          <!-- Schedule -->
          <div class="form-group">
              <label for="schedule">Schedule</label>
              <input id="schedule" type="text" name="schedule">
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
          <!-- Document -->
          <div class="form-group">
              <label for="document">Document</label>
              <input id="document" type="text" name="document">
          </div>
          <!-- Medical Information -->
          <div class="form-group">
              <label for="medinfo">Medical Information</label>
              <input id="medinfo" type="text" name="medinfo">
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

<style>
.memberAdd {
    font-family: Arial, sans-serif;
    max-width: 700px;
    margin: auto;
    padding: 20px;
    box-shadow: 0 0 10px rgba(0,0,0,0.1);
    background: #f9f9f9;
    border-radius: 8px;
}

.memberAdd h2 {
    text-align: center;
    color: #333;
}

.form-group {
    margin-bottom: 15px;
}

.form-group label {
    display: block;
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
    margin-right: 5px;
}

/* Gender Selection Styling */
.gender-radio {
    display: none; /* Hide the default radio button */
}

.form-group .gender-label {
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
