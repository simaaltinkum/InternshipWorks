using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace DataBaseProject
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void studentBindingNavigatorSaveItem_Click(object sender, EventArgs e)
        {
            this.Validate();
            this.studentBindingSource.EndEdit();
            this.tableAdapterManager.UpdateAll(this.database1DataSet);

        }

        private void Form1_Load(object sender, EventArgs e)
        {
            // TODO: Bu kod satırı 'database1DataSet.student' tablosuna veri yükler. Bunu gerektiği şekilde taşıyabilir, veya kaldırabilirsiniz.
            this.studentTableAdapter.Fill(this.database1DataSet.student);

        }

        private void genderCheckBox_CheckedChanged(object sender, EventArgs e)
        {
            if (genderCheckBox.Checked)
            {
                genderCheckBox.Text = "Erkek";            
            }
            else
            {
                genderCheckBox.Text = "Kadın";
            }
        }

        private void phoneMaskedTextBox_MaskInputRejected(object sender, MaskInputRejectedEventArgs e)
        {

        }

        private void adressTextBox_TextChanged(object sender, EventArgs e)
        {

        }
    }
}
