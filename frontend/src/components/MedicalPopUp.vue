<template>  
    <!-- Button trigger modal -->
    <button type="button" class="btn btn-primary" data-toggle="modal" data-target="#AddAppointment">
      Add Appointment
    </button>
    
    <!-- Modal -->
    <div class="modal fade" id="AddAppointment" tabindex="-1" role="dialog" aria-labelledby="MedicalModalLabel" aria-hidden="true">
      <div class="modal-dialog modal-dialog-centered" role="document">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="MedicalModalLabel">Add Appointment</h5>
            <button type="button" class="close" data-dismiss="modal" aria-label="Close">
              <span aria-hidden="true">&times;</span>
            </button>
          </div>
            <!-- Modal Body -->
        <form id="appoinmentadd" method="post" action="#">
            <div class="modal-body">
    
                <!-- Appointment Name -->
                <div class="form-group">
                    <label for="name">Appoinment Name</label>
                    <input type="text" class="form-control" id="name" placeholder="Enter appointmnet name">
                </div>

                <!-- Appointment Date -->
                <div class="form-row">
                    <div class="col-4">
                    <label for="apmdate">Appointment Date</label>
                    <input type="date" id="apmdate" class="form-control">
                    </div>
                    <div class="col-3">
                    <label for="time">Time</label>
                    
                    <select id="time" class="form-control">
                        <option selected>12:00 AM</option>
                        <option>1:00 PM</option>
                    </select>
                    </div>
                </div>
    
                <!-- Location -->
                <div class="form-group">
                    <label for="location">Location</label>
                    <input type="text" class="form-control" id="location">
                </div>
            </div>
            <div class="modal-footer">
                <button type="button" class="btn btn-primary">Submit</button>
                <button type="button" class="btn btn-secondary" data-dismiss="modal">Cancel</button>
            </div>
        </form>
        </div>
      </div>
    </div>
    </template>
    