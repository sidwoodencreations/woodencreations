import { Component, inject } from '@angular/core';
import { MatDialogRef, MatDialogModule } from '@angular/material/dialog';
import { MatButtonModule } from '@angular/material/button';
import { FormGroup, FormControl, Validators, FormsModule, ReactiveFormsModule } from '@angular/forms';
import { MatSnackBar, MatSnackBarModule } from '@angular/material/snack-bar';

@Component({
  selector: 'app-contact-dialog',
  imports: [
    MatButtonModule, 
    MatDialogModule, 
    FormsModule,
    ReactiveFormsModule,
    MatSnackBarModule
  ],
  templateUrl: './contact-dialog.component.html',
  styleUrl: './contact-dialog.component.css',
  standalone: true,
})
export class ContactDialogComponent {
  public dialogRef: MatDialogRef<ContactDialogComponent> = inject(MatDialogRef<ContactDialogComponent>);
  private snackBar = inject(MatSnackBar);

  public queryForm = new FormGroup({
    name: new FormControl('', Validators.required),
    email: new FormControl('', [Validators.required, Validators.email]),
    phoneNumber: new FormControl('', [Validators.required, Validators.pattern(/^\d{10}$/)]),
    query: new FormControl('', Validators.required),
  });

  onCancel(): void {
    this.dialogRef.close();
  }

  onSubmit(): void {
    if (this.queryForm.valid) {
      const formData = this.queryForm.value;
      console.log('Form submitted:', formData);
      this.snackBar.open(`We'll be in contact`, 'Close', {
        duration: 3000,
        panelClass: ['bg-green-600', 'text-white']
      });
      this.dialogRef.close();
    } else {
      this.snackBar.open('Please fill in all fields', 'Close', {
        duration: 3000,
        panelClass: ['bg-red-600', 'text-white']
      });
    }
  }
}
