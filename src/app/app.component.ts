import { Component, inject, OnInit } from '@angular/core';
import { MatDialog } from '@angular/material/dialog';
import { ContactDialogComponent } from './components/contact-dialog/contact-dialog.component';


@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrl: './app.component.css',
  standalone: true,
})
export class AppComponent implements OnInit {
  images: string[] = [];

  private dialog = inject(MatDialog);

  ngOnInit() {
    for(let i = 1; i <= 34; i++) {
      this.images.push(`img-${i}.jpg`);
    }
    console.log(this.images);
  }

  openContactDialog(): void {
    this.dialog.open(ContactDialogComponent, {
      width: '400px',
    });
  }
}
