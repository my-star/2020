/*
 * Created by SharpDevelop.
 * User: xuhailiang
 * Date: 2020/7/23
 * Time: 10:23
 * 
 * To change this template use Tools | Options | Coding | Edit Standard Headers.
 */
using System;
using System.Collections.Generic;
using System.Drawing;
using System.Windows.Forms;
using System.Data;
using System.Data.SqlClient;

namespace sql
{
	/// <summary>
	/// Description of MainForm.
	/// </summary>
	public partial class MainForm : Form
	{
		
		//mycon.Open();
		
		public MainForm()
		{
			
			//
			// The InitializeComponent() call is required for Windows Forms designer support.
			//
			InitializeComponent();
			
			//if (mycon.State == ConnectionState.Open){
			//	label1.Text="LinkSuccess!";
			//}
			//else 
			//	label1.Text="LinkFault!";
			//mycon.Close();
			//if(mycon.State == ConnectionState.Closed){
			//	label2.Text="CloseSuccess!";
			//}
			//
			// TODO: Add constructor code after the InitializeComponent() call.
			//
		}
		void MainFormLoad(object sender, EventArgs e)
		{
			string con="server=192.168.117.31;uid=sa;pwd=123;database=mat";
			SqlConnection mycon =new SqlConnection(con);
			mycon.Open();
			string sql="select * from pc";
			SqlDataAdapter dap = new SqlDataAdapter(sql,mycon);//create sql connect to sqldb
			DataSet ds = new DataSet();
			dap.Fill(ds);
			int count = ds.Tables[0].Columns.Count;
			string[] arylist = new string[count];
			for (int i=0;i<count;i++){
				arylist[i]=ds.Tables[0].Columns[i].ColumnName;
			}
			for(int j=0;j<count;j++){
				comboBox1.Items.Add(arylist[j]);
			}
			dataGridView1.DataSource=ds.Tables[0].DefaultView;
			comboBox1.SelectedIndex=comboBox1.Items.IndexOf(arylist[0]);
		}
		/*void Button1Click(object sender, EventArgs e)
		{
			string con="server=192.168.117.31;uid=sa;pwd=123;database=mat";
			SqlConnection mycon =new SqlConnection(con);
			mycon.Open();
			string sql="select * from pc";
			SqlDataAdapter dap = new SqlDataAdapter(sql,mycon);
			DataSet ds = new DataSet();
			dap.Fill(ds);
			dataGridView1.DataSource=ds.Tables[0].DefaultView;
		}
		*/
		
		
	}
}
